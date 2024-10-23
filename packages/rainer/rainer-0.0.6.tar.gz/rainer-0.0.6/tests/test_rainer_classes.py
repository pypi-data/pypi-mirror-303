import os
from rainer.rainer_classes import Rainer

# todo: use a different dataset in the future

# define files
data_path = "C:\\Users\\Hendrik Mattern\\Downloads\\ismrm25_nii"
fn_nii = os.path.join(data_path, "MR251201_22_hm_ep2d_mreg_fsat_12_200.nii.gz")

# define parameters
detrend_order = 2
spect_window_name = "hanning"
n_dummies = 150

# call rainer
rainer = Rainer(nii_filename=fn_nii, tr_in_sec=0.2,
                detrend_order=detrend_order,
                spect_window_name=spect_window_name,
                spect_n_dummy_volumes=n_dummies)

rainer.load_nii()

rainer.calc_detrend_data()

rainer.calc_spectrum()

rainer.save_spect_as_nii("test_spect.nii.gz")
