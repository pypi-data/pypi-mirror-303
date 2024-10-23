import numpy as np
from HSTI import fpi_sim_matrix
import sys
from scipy import interpolate as sci_inter
import string
import pickle

def ms2wl(mirror_seps, lams, camera_response, mirror_sep_spec, correction_factor=1.5e4):

    trans_matrix = fpi_sim_matrix.FPI_trans_matrix(mirror_seps, lams, 293)

    if type(camera_response) == str:
        sys.modules['scipy.interpolate._interpolate'] = sci_inter
        with open(camera_response, 'rb') as f:
            interpolate_response = pickle.load(f)
        del sys.modules['scipy.interpolate._interpolate']
        camera_response = interpolate_response(lams)
        trans_matrix = trans_matrix*camera_response[np.newaxis,:]
    elif (type(camera_response) == np.ndarray) and (len(camera_response) == len(lams)):
        camera_response = camera_response
        trans_matrix = trans_matrix*camera_response[np.newaxis,:]
    else:
        print('Camera response bust either be a string pointing to a .pkl file containing \
        the calibration curve, or be a numpy vector with the same length as the wavelength axis.')

    correction_matrix = np.zeros([trans_matrix.shape[1], trans_matrix.shape[1]])
    for j in range(trans_matrix.shape[1]):
        correction_matrix[j,j] = 2
        if j != 0:
            correction_matrix[j,j-1] = -1
        if j != trans_matrix.shape[1]-1:
            correction_matrix[j,j+1] = -1

    lams_diff = np.diff(lams)
    lams_diff = np.append(lams_diff, lams_diff[-1])
    trans_matrix = trans_matrix*lams_diff[np.newaxis,:]
    trans_matrix = trans_matrix/np.max(trans_matrix)

    ws_spec = np.linalg.inv(trans_matrix.T@trans_matrix + correction_factor*correction_matrix)@trans_matrix.T@mirror_sep_spec
    ws_spec = ws_spec/np.max(ws_spec)
    return ws_spec