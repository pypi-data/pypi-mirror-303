import numpy as np

def dsc2np(file_location):

	with open(file_location, 'r') as file:
	    lines = file.readlines()
	    
	    #Find positions of where the header ends and the footer begins. 
	    #Then load these into their own lists
	    header_idx = 0
	    footer_idx = 0

	    #The header ends where the data starts:
	    while lines[header_idx] != '1) DSC 8500 Temperature Scan \n':
	        header_idx += 1
	    header = lines[0:header_idx]
	    
	    #The first line of the footer
	    while lines[footer_idx] != '\tDSC8500 MANUAL TUNE CALIBRATION VALUES: \n':
	        footer_idx += 1
	    footer = lines[footer_idx:]
	    
	    #The steps in the recipe are compiled into its own list
	    run_steps = []
	    #Find position of first step
	    for i in range(len(header)):
	        if '1)' in header[i]:
	            first_step_idx = i
	    #Find the remaining steps
	    for i in range(first_step_idx,len(header)-1):
	        if ')' in header[i]:
	            run_steps.append(header[i])
	            
	    #The index of the recipe steps inside the main data block 
	    run_step_idx = []
	    j = 0
	    for i in range(header_idx,footer_idx):
	        if run_steps[j].split("\t")[0] in lines[i]:
	            run_step_idx.append(i)
	            if j < len(run_steps)-1:
	                j += 1
	    
	    #Labels of the columns of the output matrices
	    explination = ['Time [min]', 'Unsubtracted Heat Flow [mW]', 'Baseline Heat Flow [mW]', 'Program Temperature [°C]',\
	                  'Sample Temperature [°C]', 'Approx. Gas Flow [-]', 'Heat FLow Calibration [-]', 'Uncorrected Heat Flow [mW]']
	    
	    #A numpy array is generated for each recipe step (entry in run_steps)
	    numpy_blocks = []
	    for i in range(len(run_steps)):
	        if i == 0:
	            block = lines[run_step_idx[i]+3 : run_step_idx[i+1]]
	        elif i == len(run_steps) -1:
	            block = lines[run_step_idx[i]+1 : footer_idx-2]
	        else:
	            block = lines[run_step_idx[i]+1 : run_step_idx[i+1]]
	        
	        stepsweep = np.zeros([len(block),8])
	        for j in range(stepsweep.shape[0]):
	            for k, substring in enumerate(block[j].split("\t")):
	                if substring != '' and substring != ' \n':
	                    if substring == '-1.#IND00' or substring == '-1.#IND00 \n':
	                        stepsweep[j,k-1] = np.inf
	                    else:
	                        stepsweep[j,k-1] = float(substring)
	        numpy_blocks.append(stepsweep)

	return numpy_blocks, header, footer, run_steps, explination