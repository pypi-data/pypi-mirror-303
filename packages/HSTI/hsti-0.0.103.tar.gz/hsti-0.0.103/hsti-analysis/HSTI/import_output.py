import numpy as np
import os

#This function imports the output file into one large 2D array. The first three columns (column [0:2] - both included) present the voltage supplied to each of the three piezos. 
#Column [3:5] contain the measured intensities by the three photo diodes. Column 6 contain the sensor temperature multiplied by 100. Column [7:9] contain integers which are 
#used to calculate the actual temperature of the sensor. The final three columns (if present) display the GSK voltage, the GFID voltage and Gain respectively. 
#Only the first 6 columns are recorded during initial learnings and all other values are represented by np.nan.

def import_output(path):
	temp = []
	with open(path, 'r') as file:
	    lines = file.readlines()
	    df = np.zeros([len(lines),len(lines[-1].split())])*np.nan
	    for i in range(len(lines)):
	        splits = lines[i].split()
	        for j in range(len(splits)):
	            df[i,j] = splits[j]
	    section_last_idx = np.where(np.diff(df[:,0])<0)
	    sections = [df[0:section_last_idx[0][0]+1]]
	    for i in range(len(section_last_idx[0])-1):
	        sections.append(df[section_last_idx[0][i]+1:section_last_idx[0][i+1]+1])
	    sections.append(df[section_last_idx[0][-1]+1:])
	    return sections
    # return 2+2