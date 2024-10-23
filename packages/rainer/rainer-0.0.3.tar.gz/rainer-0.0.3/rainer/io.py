# module that handles input/loading and output/saving of files

import warnings
import numpy as np
import nibabel as nib
import json


def load_nii(filename):
    return nib.load(filename)


def extract_img_as_np_from_nii(nii):
    return np.squeeze(nii.get_fdata())


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def save_np_array_as_nii(np_array, affine, header, filename):
    # todo: auto check 4th dimension
    nii = nib.Nifti1Image(np_array, affine, header)
    nib.save(nii, filename)


def save_dict_as_json(data_dict, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, ensure_ascii=False)


def save_frequency_spectrum(freq_spect, freq_bins, affine, header, basename, tr=None):
    # wrapper function to save frequency spectrum as nifti
    # basename is filename without extension (but with path)
    # takes care of the header settings
    if tr is not None:
        zooms = header.get_zooms()[:3] + (tr,)
        header.set_zooms(zooms)
    # save spectrum with the standard nii save function
    save_np_array_as_nii(freq_spect, affine, header, basename + ".nii.gz")
    # save bins with the standard json save function
    save_dict_as_json({"frequency bins": freq_bins.tolist()}, basename + ".json")


def get_spatial_resolution_from_nii_header(header):
    return header.get_zooms()[0:3]  # nibabel stores voxel size and TR in zooms


def get_temporal_resolution_from_nii_header(header):
    tr = header.get_zooms()[3]  # nibabel stores voxel size and TR in zooms; FYI: NOT always set properly !!!
    if tr == 0.0:
        warnings.warn("\nNii-Header TR is zero! \nSet manually or load from JSON file")
    return tr


