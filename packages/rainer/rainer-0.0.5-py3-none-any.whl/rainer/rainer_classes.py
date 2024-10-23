import os

from rainer import io, analyse, plot


class Rainer:

    def __init__(self, nii_filename, json_filename=None,
                 tr_in_sec=None, detrend_order=2,
                 spect_window_name="hanning", spect_norm_method="default", spect_n_dummy_volumes=0):
        # set filenames
        self.nii_filename = nii_filename
        self.basename = self.nii_filename.split(".nii")[0]
        if json_filename is not None:
            self.json_filename = json_filename
        else:
            if os.path.isfile(f"{self.basename}.json"):
                self.json_filename = f"{self.basename}.json"
        # set file variables
        self.nii = None
        self.img = None
        self.json = None
        self.img_detrend = None
        self.spect = None
        # set imaging meta data
        self.tr_in_sec = tr_in_sec
        # set detrend options
        self.detrend_order = detrend_order
        # set spectrum options
        self.spect_window_name = spect_window_name
        self.spect_norm_method = spect_norm_method
        self.spect_n_dummy_volumes = spect_n_dummy_volumes
        self.spect_from_detrended_data = None

    def load_nii(self):
        # todo: try handling
        self.nii = io.load_nii(self.nii_filename)
        self.img = io.extract_img_as_np_from_nii(self.nii)

    def load_json(self, json_filename=None):
        if json_filename:
            self.json_filename = json_filename
        # todo: try handling
        self.json = io.load_json(self.json_filename)

    # todo add global load wrapper and variable setter e.g. TR

    def save_spect_as_nii(self, output_nii_filename=None):
        if self.spect is not None:
            if output_nii_filename is None:
                output_nii_filename = os.path.join(self.basename, "_spect.nii.gz")
            io.save_np_array_as_nii(self.spect, self.nii.affine, self.nii.header, output_nii_filename)

    # todo save detrend data

    # todo save class status report
    #  include the meta variables like use detrend_img, window, detrend order ... etc

    # todo: add global save command / wrapper

    def calc_detrend_data(self, detrend_order=None):
        if detrend_order is not None:
            self.detrend_order = detrend_order
        self.img_detrend = analyse.detrend_data_4d(self.img, self.detrend_order)

    def calc_spectrum(self, use_detrended_data=True):
        # set variables depending on detrend variable
        if use_detrended_data:
            self.spect_from_detrended_data = True
            _img_4d = self.img_detrend
        else:
            self.spect_from_detrended_data = False
            _img_4d = self.img
        # compute spectrum
        self.spect = analyse.get_spectrum_4d(_img_4d, tr_in_sec=self.tr_in_sec, window_name=self.spect_window_name,
                                             normalize_spectrum=self.spect_norm_method,
                                             n_dummy_volumes=self.spect_n_dummy_volumes)




