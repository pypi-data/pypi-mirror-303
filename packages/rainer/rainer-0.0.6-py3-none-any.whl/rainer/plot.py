import matplotlib.pyplot as plt


def plot_spectrum_per_voxel(spect_per_voxel, freq_bins,
                            ax=None, label_list=None, show_plot=True, save_filename_jpg=None):
    # spect_per_voxel organized as [n_voxel, n_freq_bins]

    # figure
    if ax is None:
        fig, ax = plt.subplots()
    # plot
    for i in range(spect_per_voxel.shape[0]):
        ax.plot(freq_bins, spect_per_voxel[i, :])
    # set labels and legend
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")
    if label_list is not None:
        ax.legend(label_list)
    # save figure
    if save_filename_jpg is not None:
        plt.savefig(save_filename_jpg,
                    dpi=300,
                    format="jpg",
                    bbox_inches='tight',
                    pad_inches=0)
    # show and close figure
    if show_plot:
        plt.show()
    else:
        plt.close()
