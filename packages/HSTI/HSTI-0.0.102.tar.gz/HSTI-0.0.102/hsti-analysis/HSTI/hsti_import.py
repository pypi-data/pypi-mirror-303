import cv2 as cv
import numpy as np
import os
from natsort import natsorted

def import_data_cube(directory, file_format = '.ppm', rotate = True, verbose = False):
    """
    ########## import_data_cube ##########
This function imports images of the stated file type (.ppm by default) from the
provided directory. The functions first looks for images at the provided distination,
but if none is found it looks first for a folder named 'capture' containing
images, but if that also fails it looks for directory 'images/capture'. If all
fails, an error message is displayed. All images are sorted based on their names
using the natsorted algorithm in the natsort module before they are compiled
into a 3D numpy array with the spatial dimensions given in the first two axes,
and the spectral dimension along the third axes.
The function also prints out the dimensions of the data cube if the verbose
parameter is set.
    """

    try:
        if '.pam' in directory:
            data = np.fromfile(directory,  dtype=np.uint8)   #importing filename to data
            header = []
            i = 0
            while (header[i-8:i] != ['E','N','D','H','D','R','\r','\n']):
                header.append(chr(data[i]))
                i += 1
            #Make header into a single string and split into list of strings whenever there is a space
            string_lst = ''.join(header).replace('\r\n', ' ').split(' ') 
            N_rows = int(string_lst[string_lst.index('WIDTH')+1])
            N_wvls = int(string_lst[string_lst.index('HEIGHT')+1])
            N_cols = int(string_lst[string_lst.index('DEPTH')+1])
            imgs = np.reshape(data[i:], [N_rows ,N_cols ,N_wvls], order = 'F')
            imgs = imgs.astype(float)
        elif '.npy' in directory:
            imgs = np.load(directory)
            imgs = imgs.astype(float)

        elif (os.path.exists(directory)) and (sum([ file_format in s for s in os.listdir(directory)]) > 0):
            new_directory = directory
            imgs = []
        elif (os.path.exists(f"{directory}/capture/")) and (sum([ file_format in s for s in os.listdir(f"{directory}/capture/")]) > 0):
            new_directory = f"{directory}/capture/"
            imgs = []
        elif (os.path.exists(f"{directory}/images/capture/")) and (sum([ file_format in s for s in os.listdir(f"{directory}/images/capture/")]) > 0):
            new_directory = f"{directory}/images/capture/"
            imgs = []

        if imgs == []:
            file_lst = [elem for elem in os.listdir(new_directory) if file_format and not 'RGB' in elem]
            file_lst = natsorted(file_lst)
            if rotate:
                for img in file_lst:
                    imgs.append(np.rot90(cv.imread(f'{new_directory}{img}',cv.IMREAD_ANYDEPTH)))
            else:
                for img in file_lst:
                    imgs.append(cv.imread(f'{new_directory}{img}',cv.IMREAD_ANYDEPTH))
            imgs = np.array(imgs, dtype = 'float32')
            imgs = np.moveaxis(imgs, 0, 2)
        if verbose:
            print('Hyperspectral image shape:')
            print(imgs.shape)

    except:
        print('Chosen directory either does not exist or contains no images of provided file type')

    return imgs

    """
    ########## import_image_acquisition_settings ##########
    his function imports the image acquisition settings during the capturing event.
    The directory that the function uses as input must be the one containing the
    'images' directory.
    """
def import_image_acquisition_settings(directory, verbose = False):

    with open(f"{directory}/output.txt", 'r') as file:
        lines = file.readlines()
        temperature_lst = []
        for line in lines:
            if (len(line.split()) == 13) or (len(line.split()) == 10):
                temperature_lst.append(int(line.split()[6])/1000)
        sens_T = np.mean(temperature_lst)
        if len(lines[-1].split()) == 13:
            GSK = int(lines[-1].split()[10])
            GFID = int(lines[-1].split()[11])
            Gain = float(lines[-1].split()[12])
        else:
            GSK = None
            GFID = None
            Gain = None

    if verbose:
        print(f'Sensor temperature: {sens_T}')
        print(f'GSK: {GSK}')
        print(f'GFID: {GFID}')
        print(f'Gain: {round(Gain,2)}')

    valdict = {
      'SENS_T': sens_T,
      'GSK': GSK,
      'GFID': GFID,
      'GAIN': Gain
    }

    return valdict
