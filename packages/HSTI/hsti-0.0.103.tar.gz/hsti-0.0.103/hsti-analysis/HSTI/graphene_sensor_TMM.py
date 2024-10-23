import numpy as np

class Stack():
    def __init__(self, airgap, lam):
        self.lam0 = 10.5e-6 #central wavelength - used for calculation of thin-film thickness.
        self.temperature = 273.15+20 #The temperature is used in calculation of Ge refractive index
        self.gap = airgap #Size of the airgap between bragg mirror and gold mirror
        # self.layers = np.array([self.refrac_Ge(self.lam0, self.temperature), self.refrac_ThF4(self.lam0), self.refrac_Ge(self.lam0, self.temperature), 1,\
        # self.refrac_Ge(self.lam0, self.temperature), self.refrac_ThF4(self.lam0), self.refrac_Ge(self.lam0, self.temperature)])
        # self.layers = np.c_[self.layers, np.array([0.5*self.lam0/self.layers[0].real, 0.25*self.lam0/self.layers[1].real,  0.25*self.lam0/self.layers[2].real, self.gap,\
        # 0.25*self.lam0/self.layers[4].real, 0.25*self.lam0/self.layers[5].real, 0.5*self.lam0/self.layers[6].real])]
        self.layers = np.array([self.refrac_Ge(self.lam0, self.temperature), self.refrac_ThF4(self.lam0), self.refrac_Ge(self.lam0, self.temperature), 1.0+0.0j])
        self.layers = np.c_[self.layers, np.array([0.5*self.lam0/self.layers[0].real, 0.25*self.lam0/self.layers[1].real,  0.25*self.lam0/self.layers[2].real, self.gap])] #Refrective index in first column, thickness in the second
        self.layer_material = ['ZnSe', 'Ge', 'ThF4', 'Ge', 'Air', 'Au'] #Refrective index in first column, thickness in the second
        self.transfer_matrix = np.zeros([2,1], dtype = np.complex_)
        self.lam = lam

    def update_indices(self, lam):
        # self.layers[:,0] = np.array([self.refrac_Ge(lam, self.temperature), self.refrac_ThF4(lam), self.refrac_Ge(lam, self.temperature), 1,\
        # self.refrac_Ge(lam, self.temperature), self.refrac_ThF4(lam), self.refrac_Ge(lam, self.temperature)])
        self.layers[:,0] = np.array([self.refrac_Ge(lam, self.temperature), self.refrac_ThF4(lam), self.refrac_Ge(lam, self.temperature), 1.0+0.0j])

    def set_airgap(self, gap):
        self.layers[-1,1] = gap
        self.stack_transfer_matrix(self.lam)

    def set_wavelength(self, lam):
        self.lam = lam
        self.stack_transfer_matrix(self.lam)

    def stack_transfer_matrix(self, lam):
        self.update_indices(lam)
        self.transfer_matrix = self.interface(self.refrac_ZnSe(lam), self.layers[0,0]) @ self.ac_phase(self.layers[0,0],self.layers[0,1].real, lam)
        for i in np.arange(1, len(self.layers[:,0]), 1):
            self.transfer_matrix = self.transfer_matrix @ self.interface(self.layers[i-1,0], self.layers[i,0]) @ self.ac_phase(self.layers[i,0], self.layers[i,1].real, lam)
        self.transfer_matrix = self.transfer_matrix @ self.interface(self.layers[-1,0], self.refrac_Au(lam))#The final layer is gold

        return self.transfer_matrix

    def transmittance(self, lam):
        M = self.stack_transfer_matrix(lam)
        return abs(1/M[0,0])**2

    def reflectance(self):
        M = self.stack_transfer_matrix(lam)
        return np.abs(M[1,0]/M[0,0])**2

    def loss(self):
        M = self.stack_transfer_matrix(lam)
        return 1 - abs(1/M[0,0])**2 - np.abs(M[1,0]/M[0,0])**2

    def refrac_ThF4(self, lam):
        # Handbook of Optical Constants of Solids II, 1998, page 1051
        lam = lam * 1e6
        n = 1.118 + 2.46 / lam - 2.98 / (lam**2)
        return n

    def refrac_ZnSe(self, lam):
        # Handbook of Optical Constants of Solids II, page 737
        lam = lam * 1e6
        n = np.sqrt(4 + 1.9*lam**2/(lam**2 - 0.113))
        return n

    def refrac_Ge(self, lam, temp):
        # Handbook of Optical Constants of Solids I, page 465
        lam = lam * 1e6
        A = -6.04e-3 * temp + 11.05128
        B = 9.295e-3 * temp + 4.00536
        C = -5.392e-4 * temp + 0.599034
        D = 4.151e-4 * temp + 0.09145
        E = 1.51408 * temp + 3426.5
        n = np.sqrt(A + (B * lam**2) / (lam**2 - C) + (D * lam**2) / (lam**2 - E))
        return n
    def refrac_Au(self,lam):
        # https://youtu.be/R8GnW2vTooM?t=1301 for conversion from permitivity to refractive index
        # The optical properties of gold are given in https://opg.optica.org/ao/fulltext.cfm?uri=ao-22-7-1099&id=26571
        wp = 7.25e4
        wt = 2.16e2
        w = 1e-2/lam #[1/cm]
        e1 = 1-wp**2/(w**2 + wt**2)
        e2 = (wp**2*wt)/(w**3+w*wt**2)

        n_real = np.sqrt((e1 + np.sqrt(e1**2 + e2**2))/2)
        k = e2/(2*n_real)

        return n_real + 1.0j*k


    def interface(self, n1, n2):
        #n1 is refractive index of leftmost film, while n2 is refracive index of rightmost film
        D = np.zeros([2,2], dtype = np.complex_)
        D[0, 0] = 1 + n2 / n1
        D[0, 1] = 1 - n2 / n1
        D[1, 0] = 1 - n2 / n1
        D[1, 1] = 1 + n2 / n1
        D = 0.5 * D
        return D

    def ac_phase(self, n, d, lam):
        P = np.zeros([2,2], dtype = np.complex_)
        P[0,0] = np.exp(1j * n * 2 * np.pi * d / lam)
        P[1, 1] = np.exp(-1j * n * 2 * np.pi * d / lam)
        return P

    def E_at_x(self, lam, x):
        self.stack_transfer_matrix(lam)
        if x > np.sum(self.layers[:,1].real):
            return np.nan
        else:
            temp = 0
            layer_nb = 0
            for i in range(len(self.layers[:,1])):
                temp += self.layers[i,1].real
                if temp >= x:
                    layer_nb = i
                    break

        d = np.sum(self.layers[0:layer_nb+1,1].real) - x #remaining distance of that layer

        if layer_nb < len(self.layers[:,0])-1:
            M = self.ac_phase(self.layers[layer_nb,0], d, lam) @ self.interface(self.layers[layer_nb,0],self.layers[layer_nb+1,0])
            for i in np.arange(layer_nb+1, len(self.layers[:,0])-1):
                M = M @ self.ac_phase(self.layers[i,0], self.layers[i,1].real, lam) @ self.interface(self.layers[i,0], self.layers[i+1,0])
            M = M @ self.ac_phase(self.layers[-1,0], self.layers[-1,1].real, lam) @ self.interface(self.layers[-1,0], self.refrac_Au(lam))
        else:
            M = self.ac_phase(self.layers[layer_nb,0], d, lam) @ self.interface(self.layers[-1,0], self.refrac_Au(lam))

        E0 = np.ones([2,1], dtype = np.complex_)
        EN = np.zeros([2,1], dtype = np.complex_)
        EN[0,0] = E0[0,0]/self.transfer_matrix[0,0]
        E0[1,0] = self.transfer_matrix[1,0]*EN[0,0]

        E = np.ones([2,1], dtype = np.complex_)
        E[0,0] = M[0,0]*EN[0,0]
        E[1,0] = M[1,0]*EN[0,0]
        return E
