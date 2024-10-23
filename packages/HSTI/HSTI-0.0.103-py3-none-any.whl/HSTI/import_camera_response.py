from scipy import interpolate as sci_inter
import pickle
import sys

################################################################################
################################################################################
#### Function for importing camera response saved in .pkl calibration file. ####
### The output is a scipy interp1d object which must then be supplied with  ####
################# wavelengths to generate the camera response ##################
################################################################################
################################################################################

def import_camera_response(path):
    if type(path) == str:
        sys.modules['scipy.interpolate._interpolate'] = sci_inter
        with open(path, 'rb') as f:
            interpolate_response = pickle.load(f)
        del sys.modules['scipy.interpolate._interpolate']
    else:
        print('Camera response must be a string pointing to a .pkl file containing the calibration curve.')
    return interpolate_response
