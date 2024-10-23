import numpy as np

class tmm_stack():
    def __init__(self, lam = 10e-6):
        lam0 = 10.5e-6 #central wavelength - used for calculation of thin-film thickness.
        self.temperature = 273.15+20 #The temperature is used in calculation of Ge refractive index
        self.custom_indices = False
        self.refrac_funcs = []
        self.refrac_funcs.append(self.refrac_Air)
        self.refrac_funcs.append(self.refrac_Ge)
        # self.refrac_funcs.append(self.refrac_ZnS)
        self.refrac_funcs.append(self.refrac_ThF4)
        # self.refrac_funcs.append(self.refrac_ZnS)
        self.refrac_funcs.append(self.refrac_Ge)
        self.refrac_funcs.append(self.refrac_ZnSe)
        self.indices = np.zeros(len(self.refrac_funcs), dtype = np.complex_)
        self.update_indices(lam0)
        self.thicknesses = np.array([np.inf, 510e-9, 1785e-9, 1255e-9, np.inf])
        self.materials = ['Air', 'Ge', 'ZnS', 'ThF4', 'ZnS', 'Ge', 'ZnSe'] #Refrective index in first column, thickness in the second
        # self.transfer_matrix = np.zeros([2,1], dtype = np.complex_)
        self.transfer_matrix = self.calculate_transfer_matrix()
        self.lam = lam

    #This function updates the refractive indices to match the inpu vacuum wavelength, lam. This also updates the system global wavelength, If no input is given, then nothing changes
    def update_indices(self, lam = None):
        if self.custom_indices == False:
            if lam != None:
                self.lam = lam
            for i in range(len(self.refrac_funcs)):
                self.indices[i] = self.refrac_funcs[i](self.lam)

    #This function calculates the system transfer matrix using Transfer Matrix Method. 
    def calculate_transfer_matrix(self, lam = None):
        if lam == None:
            lam = self.lam
        else:
            self.lam = lam
            self.update_indices(lam)
        self.transfer_matrix = self.interface(self.indices[0], self.indices[1]) @ self.ac_phase(self.indices[1],self.thicknesses[1], lam)
        for i in np.arange(2, len(self.thicknesses[:])-1):
            self.transfer_matrix = self.transfer_matrix @ self.interface(self.indices[i-1], self.indices[i]) @ self.ac_phase(self.indices[i], self.thicknesses[i], lam)
        self.transfer_matrix = self.transfer_matrix @ self.interface(self.indices[-2], self.indices[-1])
        return self.transfer_matrix

    #This function calculates the transmittance of the stack at the supplied wavelength. If no wavelength is given, then the transmittance is calculated for the current system wide wavelength. 
    def transmittance(self, lam = None):
        if lam == None:
            lam = self.lam
            M = self.transfer_matrix
        else: 
            M = self.calculate_transfer_matrix(lam)
        return abs(1/M[0,0])**2

    #This function calculates the reflectance of the stack at the supplied wavelength. If no wavelength is given, then the reflectance is calculated for the current system wide wavelength. 
    def reflectance(self, lam = None):
        if lam == None:
            lam = self.lam
            M = self.transfer_matrix
        else: 
            M = self.calculate_transfer_matrix(lam)
        return np.abs(M[1,0]/M[0,0])**2

    #This function calculates (1-transmittance-reflectance) of the stack at the supplied wavelength. If no wavelength is given, then the difference is calculated for the current system wide wavelength. 
    def loss(self, lam = None):
        if lam == None:
            lam = self.lam
            M = self.transfer_matrix
        else: 
            M = self.calculate_transfer_matrix(lam)
        return 1 - abs(1/M[0,0])**2 - np.abs(M[1,0]/M[0,0])**2

    #This funcion calculates the refractive index of ThF4 at the supplied wavelength. If no wavelength is passed on, the function uses the system wide wavelength.
    def refrac_ThF4(self, lam = None):
        # Handbook of Optical Constants of Solids II, 1998, page 1051
        if lam == None:
            lam = self.lam
        lam = lam * 1e6
        return 1.118 + 2.46 / lam - 2.98 / (lam**2) - 0.0j

    #This funcion calculates the refractive index of ZnSe at the supplied wavelength. If no wavelength is passed on, the function uses the system wide wavelength.
    def refrac_ZnSe(self, lam = None):
        if lam == None:
            lam = self.lam 
        # Handbook of Optical Constants of Solids II, page 737
        lam = lam * 1e6
        return np.sqrt(4 + 1.9*lam**2/(lam**2 - 0.113)) - 0.0j

    #This funcion calculates the refractive index of Ge at the supplied wavelength. If no wavelength is passed on, the function uses the system wide wavelength.
    def refrac_Ge(self, lam = None):
        if lam == None:
            lam = self.lam
        # Handbook of Optical Constants of Solids I, page 465
        lam = lam * 1e6
        A = -6.04e-3 * self.temperature + 11.05128
        B = 9.295e-3 * self.temperature + 4.00536
        C = -5.392e-4 * self.temperature + 0.599034
        D = 4.151e-4 * self.temperature + 0.09145
        E = 1.51408 * self.temperature + 3426.5
        return np.sqrt(A + (B * lam**2) / (lam**2 - C) + (D * lam**2) / (lam**2 - E)) - 0.0j

    #This funcion calculates the refractive index of ZnS at the supplied wavelength. If no wavelength is passed on, the function uses the system wide wavelength.
    def refrac_ZnS(self, lam = None):
        if lam == None:
            lam = self.lam
        # https://refractiveindex.info/?shelf=main&book=ZnS&page=Debenham
        lam = lam * 1e6
        return np.sqrt(8.393 + 0.14383/(lam**2 - 0.2421**2) + 4430.99/(lam**2 - 36.71**2)) - 0.0j

    #This funcion calculates the refractive index of air at the supplied wavelength. If no wavelength is passed on, the function uses the system wide wavelength.
    def refrac_Air(self, lam = None):
        if lam == None:
            lam = self.lam
        return 1.0 - 0.0j

    #This function is used to calculate the light behaviour at a material interface. n1 is refractive index of leftmost film, while n2 is refracive index of rightmost film
    def interface(self, n1, n2):
        D = np.array([[0+0j,0+0j], [0+0j,0+0j]])
        D[0, 0] = 1 + n2 / n1
        D[0, 1] = 1 - n2 / n1
        D[1, 0] = 1 - n2 / n1
        D[1, 1] = 1 + n2 / n1
        D = 0.5 * D
        return D

    #This function calculates the accumulated phase as the light travels a distance d through a material with refractive index n. lam is the vacuum wavelength.
    def ac_phase(self, n, d, lam = None):
        if lam == None:
            lam = self.lam
        P = np.array([[0+0j,0+0j], [0+0j,0+0j]])
        P[0,0] = np.exp(1j * n * 2 * np.pi * d / lam)
        P[1, 1] = np.exp(-1j * n * 2 * np.pi * d / lam)
        return P

    #This function flips the list of layers in the stack. This should not make a difference to the plots, but might be usefull in other circumstances 
    def flip_stack(self):
        self.indices = np.flip(self.indices)
        self.thicknesses = np.flip(self.thicknesses)
        self.materials.reverse()
        self.refrac_funcs.reverse()

    #This function calculates the transfer matrix at a specific point inside the stack
    def transfer_matrix_at_x(self, x, lam = None):
        if lam == None:
            lam = self.lam
        self.calculate_transfer_matrix(lam)
        if (x > np.sum(self.thicknesses[1:-1])) | (x < 0): #make sure x is within the stack
            return np.nan
        else:
            temp = 0
            layer_nb = 1 #starting at 1 since layer 0 (and the last as well) is infinite
            for i in np.arange(1, len(self.thicknesses)-1): #Count which layer x is in
                temp += self.thicknesses[i]
                if temp >= x:
                    layer_nb = i
                    break

        d = np.sum(self.thicknesses[1:layer_nb+1]) - x #remaining distance of that layer
        
        #Calculate transfer matrix for the rest of the stack to the right of x
        if layer_nb < len(self.indices[:])-2:
            M = self.ac_phase(self.indices[layer_nb], d, lam) @ self.interface(self.indices[layer_nb],self.indices[layer_nb+1])
            for i in np.arange(layer_nb+1, len(self.indices)-2):
                M = M @ self.ac_phase(self.indices[i], self.thicknesses[i], lam) @ self.interface(self.indices[i], self.indices[i+1])
            M = M @ self.ac_phase(self.indices[-2], self.thicknesses[-2], lam) @ self.interface(self.indices[-2], self.indices[-1])
        else:
            M = self.ac_phase(self.indices[layer_nb], d, lam) @ self.interface(self.indices[layer_nb], self.indices[-1])
        return M

    #This function calculates the electric field of the rightward and leftward traveling wave at a point, x, inside the stack. 
    def E_at_x(self, x, lam = None):
        M = self.transfer_matrix_at_x(x, lam)
        
        E0 = np.ones([2,1], dtype = np.complex_) #Electric field to the left of the stack
        EN = np.zeros([2,1], dtype = np.complex_) #Electric field to the right of the stack
        EN[0,0] = E0[0,0]/self.transfer_matrix[0,0]
        E0[1,0] = self.transfer_matrix[1,0]*EN[0,0]

        E = np.ones([2,1], dtype = np.complex_)
        E[0,0] = M[0,0]*EN[0,0] #Rightwards traveling E-field
        E[1,0] = M[1,0]*EN[0,0] #Leftwards traveling E-field
        return E

    #This function can be used to set the system wide wavelength of the system. When this is done, the refracrtive indices and transfer matrix is also updated.
    def set_wavelength(self, lam):
        self.lam = lam
        self.update_indices(lam)
        _ = self.calculate_transfer_matrix(lam)

    #This function can be used to pass a 1D numpy array of layer thicknesses. 
    def set_thicknesses(self, array_1D):
        self.thicknesses = array_1D

    #This function can be used to pass a list of strings containing names of each material in the stack. 
    def set_materials(self, list_of_strings):
        self.materials = list_of_strings

    #This function can be used to manually set the refractive indices of the stack. This is passed in as a numpy array. 
    def set_indices(self, array_1D):
        self.custom_indices = True
        self.indices = array_1D

    #This function is used to add additional refractive index functions. The function name is simply passed to this function which then appends it to a list. The functions should only take 
    #a single input (wavelength in meters) and give a single output (complex refractive index.)
    def add_refractive_funcs(self, function):
        self.refrac_funcs.append(function)

    #The germanium layers have temperature dependent refrective index. This function sets the system wide temperature. 
    def set_temperature(self, temperature):
        self.temperature = temperature

    #This function clears all information about the stack and resets it. It must then be built from scratch.
    def clear_stack(self):
        self.refrac_funcs = []
        self.indices = np.array([])
        self.thicknesses = np.array([])
        self.materials = []
        self.custom_indices = False
