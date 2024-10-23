import numpy as np
from IPython.display import clear_output
import concurrent.futures as cf
import pkg_resources
import pickle

def fpi_trans_single_mirror_sep(wavelength, temp, layer_t):
    transmittance_vec = np.zeros_like(wavelength)
    for idx, wvl in enumerate(wavelength):
        stack_refractive_index = np.array([refrac_Ge(wvl, temp), refrac_ThF4(wvl), refrac_Ge(wvl, temp), 1, refrac_Ge(wvl, temp), refrac_ThF4(wvl), refrac_Ge(wvl, temp)], dtype = np.complex_)
        T = transfer_FPI(stack_refractive_index, layer_t, wvl)
        transmittance_vec[idx] = abs(1/T[0,0])**2
    return transmittance_vec

def FPI_trans_matrix(mirror_sep, lam, temperature):
    lam0 = 10.5e-6 #Central wavelength used for layer thicknesses

    transmittance = np.zeros([len(mirror_sep), len(lam)] , dtype = np.complex_)
    layer_thickness = np.array([0.5*lam0/refrac_Ge(lam0, temperature).real, 0.25*lam0/refrac_ThF4(lam0).real,  0.25*lam0/refrac_Ge(lam0, temperature).real, 0, 0.25*lam0/refrac_Ge(lam0, temperature).real, 0.25*lam0/refrac_ThF4(lam0).real, 0.5*lam0/refrac_Ge(lam0, temperature).real])

    #Formulate input into lists for later multiprocessing
    lam_lst, temperature_lst, layer_thickness_lst, = [], [], []
    for m_sep in mirror_sep:
        lam_lst.append(lam)
        temperature_lst.append(temperature)
        temp_layer_thickness = np.copy(layer_thickness)
        temp_layer_thickness[3] = m_sep
        layer_thickness_lst.append(temp_layer_thickness)


    with cf.ProcessPoolExecutor() as executor:
        results = executor.map(fpi_trans_single_mirror_sep, lam_lst, temperature_lst, layer_thickness_lst)

    for i, result in enumerate(results):
        transmittance[i,:] = result
    return transmittance

def refrac_ThF4(lam):

    resource_package = __name__
    resource_path = '/'.join(('HSTI_data_files-main', 'ThF4_extinction_coeff_fit.pkl'))  # Do not use os.path.join()
    path = pkg_resources.resource_stream(resource_package, resource_path)
    interpolated = pickle.load(path)
    ThF4_k_interp = interpolated(lam)

    # Handbook of Optical Constants of Solids II, 1998, page 1051
    lam = lam * 1e6
    n = 1.118 + 2.46 / lam - 2.98 / (lam**2) - ThF4_k_interp*1j
    return n

def refrac_ZnSe(lam):
    # Handbook of Optical Constants of Solids II, page 737
    lam = lam * 1e6
    n = np.sqrt(4 + 1.9*lam**2/(lam**2 - 0.113)) - 0j
    return n

def refrac_Ge(lam, temperature):
    # Handbook of Optical Constants of Solids I, page 465
    lam = lam * 1e6
    A = -6.04e-3 * temperature + 11.05128
    B = 9.295e-3 * temperature + 4.00536
    C = -5.392e-4 * temperature + 0.599034
    D = 4.151e-4 * temperature + 0.09145
    E = 1.51408 * temperature + 3426.5
    n = np.sqrt(A + (B * lam**2) / (lam**2 - C) + (D * lam**2) / (lam**2 - E)) - 0j
    return n

def transfer_FPI(n, d, lam):
    T = interface(refrac_ZnSe(lam), n[0]) @ ac_phase(n[0], d[0], lam)
    for i in np.arange(1, len(n), 1):
        T = T @ interface(n[i-1], n[i]) @ ac_phase(n[i], d[i], lam)
    T = T @ interface(n[-1], refrac_ZnSe(lam))
    return T

def interface(n1, n2):
    #n1 is refractive index of leftmost film, while n2 is refracive index of rightmost film
    D = np.ones([2,2], dtype = np.complex_)
    D[0, 0] = 1 + n2 / n1
    D[0, 1] = 1 - n2 / n1
    D[1, 0] = 1 - n2 / n1
    D[1, 1] = 1 + n2 / n1
    D = 0.5 * D
    return D

def ac_phase(n, d, lam):
    P = np.array([[0+0j,0+0j], [0+0j,0+0j]], dtype = np.complex_)
    P[0,0] = np.exp(1j * n * 2 * np.pi * d / lam)
    P[1, 1] = np.exp(-1j * n * 2 * np.pi * d / lam)
    return P
