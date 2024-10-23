import numpy as np
import sys
from HSTI import fpi_sim_matrix
import os
import string
from scipy import interpolate as sci_inter
import pickle

################################################################################
################################################################################
## Class for performing FPI calculations such as converting from FTIR to FPI ###
## spectra or vice versa. All is based on the assumption of loss less mirrors ##
################################################################################
################################################################################


class FPI:
    def __init__(self, mirror_seps = [], lams = [], temperature = None):
        self.trans_matrix = []
        self.__original_trans_matrix = []
        self.mirror_seps = mirror_seps
        self.lams = lams
        self.temperature = temperature
        self.camera_response = []
        if (self.lams is not []) and (self.mirror_seps is not []) and (self.temperature is not None):
            self.trans_matrix = fpi_sim_matrix.FPI_trans_matrix(self.mirror_seps, self.lams, self.temperature)

    def set_trans_matrix(self, trans_matrix):
        self.trans_matrix = trans_matrix

    def set_mirror_seps(self, mirror_seps):
        self.mirror_seps = mirror_seps

    def set_wavelengths(self, lams):
        self.lams = lams

    def get_trans_matrix(self):
        return self.trans_matrix

    def get_mirror_seps(self):
        return self.mirror_seps

    def get_wavelengths(self):
        return self.lams

    def wl2ms(self, wavelength_spec):
        if self.trans_matrix is not []:
            lams_diff = np.diff(self.lams)
            lams_diff = np.append(lams_diff, lams_diff[-1])
            temp_trans_matrix = np.copy(self.trans_matrix)
            temp_trans_matrix = temp_trans_matrix*lams_diff

            ms_spec = temp_trans_matrix@wavelength_spec
            return ms_spec
        else:
            print('A transmission matrix must first be calculated or supplied')

    def ms2wl(self, mirror_sep_spec, correction_factor=1.5e4):
        correction_matrix = np.zeros([self.trans_matrix.shape[1], self.trans_matrix.shape[1]])
        for j in range(self.trans_matrix.shape[1]):
            correction_matrix[j,j] = 2
            if j is not 0:
                correction_matrix[j,j-1] = -1
            if j is not self.trans_matrix.shape[1]-1:
                correction_matrix[j,j+1] = -1

        lams_diff = np.diff(self.lams)
        lams_diff = np.append(lams_diff, lams_diff[-1])
        temp_trans_matrix = np.copy(self.trans_matrix)
        temp_trans_matrix = temp_trans_matrix*lams_diff[np.newaxis,:]
        temp_trans_matrix = temp_trans_matrix/np.max(temp_trans_matrix)

        ws_spec = np.linalg.inv(temp_trans_matrix.T@temp_trans_matrix + correction_factor*correction_matrix)@temp_trans_matrix.T@mirror_sep_spec
        ws_spec = ws_spec/np.max(ws_spec)
        return ws_spec

    def apply_camera_response(self, camera_response = []):
        if (self.trans_matrix is not []) and (self.__original_trans_matrix == []):
            self.__original_trans_matrix = np.copy(self.trans_matrix)

            if type(camera_response) == str:
                sys.modules['scipy.interpolate._interpolate'] = sci_inter
                with open(camera_response, 'rb') as f:
                    interpolate_response = pickle.load(f)
                del sys.modules['scipy.interpolate._interpolate']
                self.camera_response = interpolate_response(self.lams)
                self.trans_matrix = self.__original_trans_matrix*self.camera_response
            elif (type(camera_response) == np.ndarray) and (len(camera_response) == len(self.lams)):
                self.camera_response = camera_response
                self.trans_matrix = self.__original_trans_matrix*self.camera_response
            else:
                print('Camera response bust either be a string pointing to a .pkl file containing \
                the calibration curve, or be a numpy vector with the same length as the wavelength axis.')
        else:
            print('A transmission matrix must first be calculated or supplied')

    def remove_camera_response(self):
        if self.__original_trans_matrix is not []:
            self.trans_matrix = self.__original_trans_matrix
            self.__original_trans_matrix = []
        else:
            print('The camera response was not applied to the transmission matrix in the first place. Nothing has been done')
