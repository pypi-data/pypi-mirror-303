import numpy as np
import os
import concurrent.futures as cf
import cv2

# Function for saving individual images in .ppm format
def save_img(img, directory):
    cv2.imwrite(directory, img)
    # Renaming the '.pgm' images to '.ppm' to follow the format coming fron the camera
    new_directory = directory[0:-2] + 'p' + directory[-2+1:]
    os.rename(directory, new_directory)

def export_data_cube(data_cube, directory, rotate = False, file_name_list = None, generate_folders = False, normalize_each_band = False):
    """
    ########## HSTI_export ##########
    This function takes an HSTI numpy array and exports it as individual .ppm
    images to a folder given by folder_name.
    """
    if generate_folders:
        if os.path.isdir(os.getcwd() + '/' + directory) == False:
            os.mkdir(os.getcwd() + '/' + directory)
            os.mkdir(os.getcwd() + '/' + directory + '/images')
            os.mkdir(os.getcwd() + '/' + directory + '/images/capture')
        new_directory = os.getcwd() + '/' + directory + '/images/capture'
    else:
        if os.path.isdir(os.getcwd() + '/' + directory) == False:
            os.mkdir(os.getcwd() + '/' + directory)
        new_directory = os.getcwd() + '/' + directory
    if rotate:
        data_cube = np.rot90(data_cube, 3)
    img_size = [data_cube.shape[0], data_cube.shape[1]]

    if normalize_each_band:
        for i in range(data_cube.shape[2]):
            data_cube[:,:,i] = 65535.9*(data_cube[:,:,i] - np.nanmin(data_cube[:,:,i]))/(np.nanmax(data_cube[:,:,i]) - np.nanmin(data_cube[:,:,i]))
    else:
        data_cube = 65535.9*(data_cube - np.nanmin(data_cube))/(np.nanmax(data_cube) - np.nanmin(data_cube))

    data_cube = data_cube.astype(np.uint16)


# setting up for multi processing
    img_lst, directory_lst = [], []
    if (file_name_list == None) or (len(file_name_list) != data_cube.shape[2]):
        for i in range(data_cube.shape[2]):
            img_lst.append(data_cube[:,:,i])
            step = i*10
            directory_lst.append(f'{new_directory}/step{step}.pgm')
    else:
        for i in range(data_cube.shape[2]):
            img_lst.append(data_cube[:,:,i])
            directory_lst.append(f'{new_directory}/{file_name_list[i]}.pgm')

# Multiprocessing step
    with cf.ProcessPoolExecutor() as executor:
        results = executor.map(save_img, img_lst, directory_lst)
