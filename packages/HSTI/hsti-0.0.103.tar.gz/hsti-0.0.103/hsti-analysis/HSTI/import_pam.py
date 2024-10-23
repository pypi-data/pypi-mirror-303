import numpy as np
def import_pam(directory):
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


	return np.reshape(data[i:], [N_rows ,N_cols ,N_wvls], order = 'F')