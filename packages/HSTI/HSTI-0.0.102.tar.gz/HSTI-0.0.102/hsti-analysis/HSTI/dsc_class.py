from BaselineRemoval import BaselineRemoval
from scipy import interpolate
import numpy as np
import os


class dsc:
	def __init__(self, path_to_txt = None):
		self.header = None
		self.footer = None
		self.run_steps = None
		self.explanations = None
		self.data_blocks = None
		self.sample_weight = None
		self.sample_ID = None
		self.stepscan = False
		self.stepscan_idx = None
		self.Nsteps = None
		self.step_start_temp = None
		self.step_size = None
		self.step_rate = None
		self.step_temperatures = None
		self.step_first_idx = None
		self.step_last_idx = None
		self.stepscan_baseline = None
		if (path_to_txt is not None) and (os.path.isfile(path_to_txt)):
			self.import_dsc_data(path_to_txt)

	def import_dsc_data(self, path_to_txt):
		with open(path_to_txt, 'r') as file:
			lines = file.readlines()
			
			#Find positions of where the header ends and the footer begins. 
			#Then load these into their own lists
			header_idx = 0
			footer_idx = 0

			#The header ends where the data starts:
			while lines[header_idx] != '1) DSC 8500 Temperature Scan \n':
				header_idx += 1
			self.header = lines[0:header_idx]
			
			#The first line of the footer
			while lines[footer_idx] != '\tDSC8500 MANUAL TUNE CALIBRATION VALUES: \n':
				footer_idx += 1
			self.footer = lines[footer_idx:]
			
			#Find the sample ID and sample weight in the header
			i = 0
			while 'Sample ID' not in self.header[i]:
				i += 1
			self.sample_ID = self.header[i].split('\t')[-1].rstrip()

			while 'Display Weight' not in self.header[i]:
				i += 1
			self.sample_weight = float(self.header[i].split('\t')[-1])*1e-6

			#The steps in the recipe are compiled into its own list
			self.run_steps = []
			#Find position of first step
			for i in range(len(self.header)):
				if '1)' in self.header[i]:
					first_step_idx = i
			#Find the remaining steps
			for i in range(first_step_idx,len(self.header)-1):
				if ')' in self.header[i]:
					self.run_steps.append(self.header[i])
					
			#The index of the recipe steps inside the main data block 
			run_step_idx = []
			j = 0
			for i in range(header_idx,footer_idx):
				if self.run_steps[j].split("\t")[0] in lines[i]:
					run_step_idx.append(i)
					if j < len(self.run_steps)-1:
						j += 1
			
			#If a step scan is performed find the number of steps and start temperature
			for i in range(len(self.run_steps)):
				if 'StepScan' in self.run_steps[i]:
					self.stepscan = True
					self.stepscan_idx = i
					self.Nsteps = int(self.run_steps[i].split(' ')[-2].split('X')[0])
					self.step_start_temp = float(self.run_steps[i].split('StepScan:')[-1].split('°C')[0])
					self.step_size = float(self.run_steps[i].split('StepScan:')[-1].split('°C')[1].split('to ')[1]) - self.step_start_temp
					self.step_rate = float(self.run_steps[i].split('@')[-1].split('°C')[0])
					self.step_temperatures = np.arange(self.step_start_temp, self.step_start_temp+self.Nsteps+1)

			#Labels of the columns of the output matrices
			self.explanations = ['Time [s]', 'Unsubtracted Heat Flow [W]', 'Baseline Heat Flow [W]', 'Program Temperature [°C]',\
						  'Sample Temperature [°C]', 'Approx. Gas Flow [-]', 'Heat FLow Calibration [-]', 'Uncorrected Heat Flow [W]']
			
			#A numpy array is generated for each recipe step (entry in run_steps)
			self.data_blocks = []
			for i in range(len(self.run_steps)): #Iterates through each data block (run_steps)
				if i == 0:
					block = lines[run_step_idx[i]+3 : run_step_idx[i+1]] #block is a list of strings
				elif i == len(self.run_steps) -1:
					block = lines[run_step_idx[i]+1 : footer_idx-2]
				else:
					block = lines[run_step_idx[i]+1 : run_step_idx[i+1]]
				
				stepsweep = np.zeros([len(block),len(self.explanations)]) 
				for j in range(stepsweep.shape[0]): #Iterate through each row of data block
					for k, substring in enumerate(block[j].split("\t")): #Split row (line) at each "\t" and iterate through each col
						if substring != '' and substring != ' \n': #Only consider non empty and non-"\n" strings
							if substring == '-1.#IND00' or substring == '-1.#IND00 \n': #If #IND00 - insert nan
								stepsweep[j,k-1] = np.nan
							else:
								stepsweep[j,k-1] = float(substring) #Else convert string to float
				
				#stepsweep now contains all data from the given recipe step. Next we replace any instances of np.nan.
				nan_idx = np.where(np.isnan(stepsweep)) # Get all indices of nans
				for j in range(len(nan_idx[0])): #iterate through indices
					k = 1
					k_increase = 1
					while np.isnan(stepsweep[nan_idx[0][j]+k, nan_idx[1][j]]):  #keep increasing k until a non-nan element is encountered
						if nan_idx[0][j]+k >= stepsweep.shape[0]: #if the index + k is larger than the length of the array, look in the other direction
							k_increase = -1
						k += k_increase
					stepsweep[nan_idx[0][j], nan_idx[1][j]] = stepsweep[nan_idx[0][j]+k, nan_idx[1][j]] #replace nan by closest non-nan

				stepsweep[:,0] = stepsweep[:,0]*60 #convert time from minutes to seconds
				stepsweep[:,1:3] = stepsweep[:,1:3]*1e-3 #convert from mW to W
				#stepsweep[:,3:5] = stepsweep[:,3:5]+273.15 #convert from C to K.
				stepsweep[:,-1] = stepsweep[:,-1]*1e-3
				self.data_blocks.append(stepsweep)

			self.header = [line.replace('\t','').rstrip() for line in self.header]
			self.footer = [line.replace('\t','').rstrip() for line in self.footer]
			self.run_steps = [line.replace('\t','').rstrip() for line in self.run_steps]

	def baseline_scan(self, data, degree): #Remove baseline of order, 'degree', from 'data' 
		BLR_obj = BaselineRemoval(data)
		baselined_data=BLR_obj.IModPoly(degree)
		return baselined_data # Should this be negative in order for heat flow exothermic up



	def baseline_stepscan(self):
		self.step_first_idx = []  #First index at which the program temperature is equal to one of the temperatures in step_temperatures
		self.step_last_idx = []   #Last index the program temperature is equal the same step temperature as in self.step_first_idx
		baseline_idx = []  #The index of the local minimum between the self.step_last_idx of previous step and self.step_first_idx of next step. This is used as the baseline of the curve
		self.step_last_idx.append(0)  #Since the starting temperature technically isn't part of a step (rather the base), the first index is added to the list
		##self.step_last_idx contains one additional idx compared to self.step_first_idx and baseline_idx.

		for i in range(len(self.step_temperatures)-1):
			self.step_first_idx.append(np.where(self.data_blocks[self.stepscan_idx][:,3] == self.step_temperatures[i+1])[-1][0])
			self.step_last_idx.append(np.where(self.data_blocks[self.stepscan_idx][:,3] == self.step_temperatures[i+1])[-1][-1])
			segment = self.data_blocks[self.stepscan_idx][self.step_last_idx[i]:self.step_last_idx[i+1],1] # Looking at an entire step
			slope = (segment[-1] - segment[0])/(self.data_blocks[self.stepscan_idx][self.step_last_idx[i+1],0] - self.data_blocks[self.stepscan_idx][self.step_last_idx[i],0]) #The slope of the line connecting the end points of the step
			temp_time = self.data_blocks[self.stepscan_idx][self.step_last_idx[i]:self.step_last_idx[i+1],0] - self.data_blocks[self.stepscan_idx][self.step_last_idx[i+1],0] #make a time axis the length of the step, starting at t = 0
			slope_correction = segment - (temp_time*slope + segment[0]) #Remove the slope from the segment
			baseline_idx.append(self.step_last_idx[i] + np.where(slope_correction == np.nanmin(slope_correction))[-1][0]) #Find the index of the minimum within the slope corrected segment. This is the baseline

		#remove the base line from the curve and perform linear interpolation at every time step 
		baseline_interp = interpolate.interp1d(self.data_blocks[self.stepscan_idx][baseline_idx,0], self.data_blocks[self.stepscan_idx][baseline_idx,1], kind = 'linear', fill_value = 'extrapolate')
		self.stepscan_baseline = self.data_blocks[self.stepscan_idx][:,1] - baseline_interp(self.data_blocks[self.stepscan_idx][:,0]) #subtract the baseline from every data point in the step scan
		return self.stepscan_baseline

		#Calculate specific heat capacity
	def calculate_cp(self):
		step_baseline_corrected = self.baseline_stepscan() #The step scan must have its baseline removed. 
		areas = []	#Calculate area of each heating step in the step scan.
		for i in range(len(self.step_temperatures)-1):
			areas.append(np.trapz(step_baseline_corrected[self.step_last_idx[i]:self.step_last_idx[i+1]], self.data_blocks[-1][self.step_last_idx[i]:self.step_last_idx[i+1],0]))
		return np.array(areas)/(self.sample_weight*self.step_size)

