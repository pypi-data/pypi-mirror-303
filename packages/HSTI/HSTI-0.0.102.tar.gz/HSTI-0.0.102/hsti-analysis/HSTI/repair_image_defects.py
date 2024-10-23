import numpy as np

def repair_bad_col(cube):
    #This function replaces two column of defected pixels on the 10_10_200_22 camera. The column indices are hard coded, and requires the image to have been rotated right side up
    #as well as still be at full size. 

     #Firstly recognize whether there are more than one image in the 'cube'       
    if len(cube.shape) == 2:
        cube = cube[:,:,np.newaxis]
        multilayer = False
    else:
        multilayer = True

    #Define indexes of all bad pixels for first column
    all_row_idx1 = np.arange(0,cube.shape[0])
    good_row_idx1 = all_row_idx1[::2]
    #... and second column
    all_row_idx2 = np.arange(950,cube.shape[0])
    good_row_idx2 = all_row_idx2[::2]
    
    #Iterate through each layer of the cube and repair
    for i in range(cube.shape[2]):
        #First column
        good_row_vals = cube[good_row_idx1,504, i]
        cube[all_row_idx1,504, i] = np.interp(all_row_idx1, good_row_idx1, good_row_vals)
        #Second column
        good_row_vals = cube[good_row_idx2,505, i]
        cube[all_row_idx2,505, i] = np.interp(all_row_idx2, good_row_idx2, good_row_vals)
    #Return input with the same shape as input
    if not multilayer:
        cube = np.squeeze(cube, 2)
    return cube

def repair_nans(cube, max_it = 100):
    #This function replaces all NaN-containing entries in a 2D numpy array and replaces them with the median value of their apparent neighborhood

    #Firstly recognize whether there are more than one image in the 'cube'
    if len(cube.shape) == 2:
        cube = cube[:,:,np.newaxis]
        multilayer = False
    else:
        multilayer = True

    # Remove NaNs from each layer in cube
    for i in range(cube.shape[2]):
        offset = 1 #The offset defines the neighborhood around the 'bad' pixel, which will be used to correct it. An offset of 1 results in a 3x3 neighborhood with the bad pixel in the center
        layer = cube[:,:,i]
        while np.isnan(layer).any(): #As long as there are NaNs do:
            [nan_row, nan_col] = np.where(np.isnan(layer)) #Get indices of bad pixels
            #If there are any edge cases, the entire image is padded with the median value, and the row and column indices are adjusted accordingly
            if np.isin(nan_row, [0,layer.shape[0]-1]).any() or np.isin(nan_col, [0,layer.shape[1]-1]).any(): 
                layer = np.pad(layer, offset, 'constant', constant_values = np.nanmedian(layer))
                nan_row += offset
                nan_col += offset
            for j in range(len(nan_row)): #Loop through every index and replace with the median of the neighborhood
                neighborhood = layer[nan_row[j]-offset:nan_row[j]+offset+1,nan_col[j]-offset:nan_col[j]+offset+1]
                layer[nan_row[j], nan_col[j]] = np.nanmedian(neighborhood) #Replace neighborhood
            offset += 1 #Offset is increased in case there are still bad pixels
            #If max number of iterations is reached, break out of loop - only here to prevent hang-ups
            if offset > max_it:
                print('Break')
                break
        #If edge cases are detected, only the original part of the image is kept - not the padding
        if layer.shape[0] != cube.shape[0]:
            layer = layer[offset - 1:-(offset - 1), offset - 1:-(offset - 1)]
        
        cube[:,:,i] = layer

    #The third dimension of the cube is removed if there is only a single layer
    if not multilayer:
        cube = np.squeeze(cube, 2)
    return cube


def remove_stuck_px(data_cube):
    temp_data_cube = np.copy(data_cube)
    min_img = np.min(data_cube, axis=2)
    zero_idx = np.where(min_img == 0)
    zero_std_idx = np.where(np.std(data_cube, axis = 2) == 0)
    for i in range(len(zero_idx[0])):
        if zero_idx[0][i] == 0 and zero_idx[1][i] == 0:  # upper left
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] + 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :]) / 3
        elif zero_idx[0][i] == 0 and zero_idx[1][i] == data_cube.shape[1]-1:  # upper right
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] + 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 3
        elif zero_idx[0][i] == data_cube.shape[0]-1 and zero_idx[1][i] == 0:  # lower left
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] - 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :]) / 3
        elif zero_idx[0][i] == data_cube.shape[0]-1 and zero_idx[1][i] == data_cube.shape[1]-1:  # lower right
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] - 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 3
        elif zero_idx[0][i] == 0:  # upper row
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] + 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 5
        elif zero_idx[0][i] == data_cube.shape[0]-1:  # lower row
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] - 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 5
        elif zero_idx[1][i] == 0:  # leftmost column
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] + 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :]) / 5
        elif zero_idx[1][i] == data_cube.shape[1]-1:  # rightmost column
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] - 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 5
        else:
            temp_data_cube[zero_idx[0][i], zero_idx[1][i], :] = (data_cube[zero_idx[0][i] + 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i] + 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i] - 1, zero_idx[1][i], :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_idx[0][i], zero_idx[1][i] - 1, :]) / 8

    for i in range(len(zero_std_idx[0])):
        if zero_std_idx[0][i] == 0 and zero_std_idx[1][i] == 0:  # upper left
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :]) / 3
        elif zero_std_idx[0][i] == 0 and zero_std_idx[1][i] == data_cube.shape[1]-1:  # upper right
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 3
        elif zero_std_idx[0][i] == data_cube.shape[0]-1 and zero_std_idx[1][i] == 0:  # lower left
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :]) / 3
        elif zero_std_idx[0][i] == data_cube.shape[0]-1 and zero_std_idx[1][i] == data_cube.shape[1]-1:  # lower right
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 3
        elif zero_std_idx[0][i] == 0:  # upper row
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 5
        elif zero_std_idx[0][i] == data_cube.shape[0]-1:  # lower row
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 5
        elif zero_std_idx[1][i] == 0:  # leftmost column
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :]) / 5
        elif zero_std_idx[1][i] == data_cube.shape[1]-1:  # rightmost column
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 5
        else:
            temp_data_cube[zero_std_idx[0][i], zero_std_idx[1][i], :] = (data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i] - 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i] + 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i] - 1, zero_std_idx[1][i], :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] + 1, :] + \
                                                                 data_cube[zero_std_idx[0][i], zero_std_idx[1][i] - 1, :]) / 8

    return temp_data_cube


def remove_outlying_px(data_cube, cut_off):
    temp_data_cube = np.copy(data_cube)
    gray_img = np.mean(temp_data_cube, axis=2)
    gray_img += abs(np.min(gray_img))
    gray_img = gray_img / np.max(gray_img)

    neighbour_img = np.zeros([gray_img.shape[0], gray_img.shape[1]])
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            if i == 0 and j == 0:  # upper left
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i, j + 1] + gray_img[i + 1, j] + gray_img[i + 1, j + 1]) / 3
            elif i == 0 and j == gray_img.shape[1] - 1:  # upper right
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i, j - 1] + gray_img[i + 1, j] + gray_img[i + 1, j - 1]) / 3
            elif i == gray_img.shape[0] - 1 and j == 0:  # bottom left
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i - 1, j] + gray_img[i, j + 1] + gray_img[i - 1, j + 1]) / 3
            elif i == gray_img.shape[0] - 1 and j == gray_img.shape[1] - 1:  # bottom right
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i, j - 1] + gray_img[i - 1, j] + gray_img[i - 1, j - 1]) / 3
            elif i == 0:  # top row
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i, j - 1] + gray_img[i, j + 1] + gray_img[i + 1, j] + gray_img[i + 1, j - 1] + gray_img[i + 1, j + 1]) / 5
            elif i == gray_img.shape[0] - 1:  # bottom row
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i, j - 1] + gray_img[i, j + 1] + gray_img[i - 1, j] + gray_img[i - 1, j - 1] + gray_img[i - 1, j + 1]) / 5
            elif j == 0:  # leftmost column
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i + 1, j] + gray_img[i - 1, j] + gray_img[i, j + 1] + gray_img[i + 1, j + 1] + gray_img[i - 1, j + 1]) / 5
            elif j == gray_img.shape[1] - 1:  # rightmost column
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i + 1, j] + gray_img[i - 1, j] + gray_img[i, j - 1] + gray_img[i + 1, j - 1] + gray_img[i - 1, j - 1]) / 5
            else:
                neighbour_img[i, j] = gray_img[i, j] - (gray_img[i - 1, j - 1] + gray_img[i - 1, j] + gray_img[i - 1, j + 1] + gray_img[i, j + 1] + gray_img[i + 1, j + 1] + gray_img[i + 1, j] + gray_img[i + 1, j - 1] + gray_img[i, j - 1]) / 8

    outlier_idx = np.where(abs(neighbour_img) > cut_off)

    for i in range(len(outlier_idx[0])):
        if outlier_idx[0][i] == 0 and outlier_idx[1][i] == 0:  # upper left
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :]) / 3
        elif outlier_idx[0][i] == 0 and outlier_idx[1][i] == data_cube.shape[1]-1:  # upper right
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 3
        elif outlier_idx[0][i] == data_cube.shape[0]-1 and outlier_idx[1][i] == 0:  # lower left
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :]) / 3
        elif outlier_idx[0][i] == data_cube.shape[0]-1 and outlier_idx[1][i] == data_cube.shape[1]-1:  # lower right
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 3
        elif outlier_idx[0][i] == 0:  # upper row
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 5
        elif outlier_idx[0][i] == data_cube.shape[0]-1:  # lower row
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 5
        elif outlier_idx[1][i] == 0:  # leftmost column
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :]) / 5
        elif outlier_idx[1][i] == data_cube.shape[1]-1:  # rightmost column
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 5
        else:
            temp_data_cube[outlier_idx[0][i], outlier_idx[1][i], :] = (data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i] - 1, :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i] + 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i] - 1, outlier_idx[1][i], :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] + 1, :] + \
                                                                 data_cube[outlier_idx[0][i], outlier_idx[1][i] - 1, :]) / 8

    return temp_data_cube, outlier_idx