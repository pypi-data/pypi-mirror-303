import warnings
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal.windows import hann, hamming, blackman
from scipy.stats import binned_statistic


def get_frequency_spectrum(image_data, tr, window_name="hanning", window=None,
                           do_detrend=True, detrend_degree=2,
                           normalize_spectrum="default", n_dummy_volumes=0):
    # computes the frequency spectrum of a 4D data set (3D + t)

    if len(image_data.shape) != 4:
        warnings.warn("\nImage data is NOT 4D\n")

    # exclude dummy volumes and compute number of measurements
    image_data = image_data[:, :, :, n_dummy_volumes:]
    n = image_data.shape[3]

    # de-trend the data: degree == 0: mean; 1: mean+linear; 2: mean+linear+quadratic, and so on
    if do_detrend:
        image_data = detrend_4d_data(image_data, detrend_degree)

    # set up window if required
    if window is None:
        if window_name.lower() == "hanning":
            window = hann(n, sym=False)
        elif window_name.lower() == "hamming":
            window = hamming(n, sym=False)
        elif window_name.lower() == "blackman":
            window = blackman(n, sym=False)
        else:
            window = np.ones(n)

    # compute complex frequency spectrum (n-measurements long, but mirrored at n/2)
    freq_spect = fft(image_data * window, axis=3)
    # take the absolute and crop/remove mirrored part
    freq_spect = np.abs(freq_spect)[:, :, :, 0:n // 2]
    # normalize frequency spectrum with selected strategy
    if normalize_spectrum.lower() == "default":
        freq_spect = 2.0 * freq_spect / n
    # frequency bins for which the FFT was computes
    freq_bins = fftfreq(n, tr)[0:n // 2]

    return freq_spect, freq_bins


def detrend_4d_data(data_4d, degree):
    # use polynomial model to de-trend data
    #  degree == 0: mean; 1: mean+linear; 2: mean+linear+quadratic, and so on
    n = data_4d.shape[3]
    # create polynomial model
    x = np.arange(0, n)  # [N]
    coef = np.polynomial.polynomial.polyfit(x, data_4d.reshape(-1, n).transpose(), degree)  # fit
    coef = coef.transpose().reshape(data_4d.shape[0], data_4d.shape[1], data_4d.shape[2], -1)  # reshape
    # remove offset / average
    data_4d = data_4d - coef[:, :, :, 0][:, :, :, np.newaxis]
    # remove higher order drifts / trends
    for i in range(1, degree + 1):
        current_coef = coef[:, :, :, i][:, :, :, np.newaxis]  # as pseudo 4D
        data_4d = data_4d - current_coef * (x ** i)  # y = y - y_est^d =  y - c * x^d
    return data_4d


def bin_freq_spect(freq_spect, freq_bins_old, freq_bins_new):  # todo: better name e.g. by adding _1d or _4d 
    # re-bin the data
    freq_spect_binned, freq_bins_new, bin_number = binned_statistic(freq_bins_old,
                                                                    freq_spect.reshape((-1, freq_spect.shape[3])),
                                                                    bins=freq_bins_new, statistic="sum")
    # todo: implement own stat function which takes the integral per bin; or do as post processing

    # reshape
    freq_spect_binned = freq_spect_binned.reshape((freq_spect.shape[0], freq_spect.shape[1], freq_spect.shape[2], -1))
    return freq_spect_binned, freq_bins_new[:-1]  # remove last element to match freq_spect dimension

