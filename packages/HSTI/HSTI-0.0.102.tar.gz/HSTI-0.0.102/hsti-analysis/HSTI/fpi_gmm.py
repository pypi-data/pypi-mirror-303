import numpy as np

def fpi_gmm(m_seps=np.array([10e-6]), lams = np.array([10e-6]), angle = 0, degrees = True, fraction_s_pol = 0.5, n_points = 7, mirror_height = 150e-9):

    if degrees == True: #Convert angle to radians
        angle = np.radians(angle)

    ### The first part is for taking the curvature of the mirrors into account, as they effectively broaden the spectra
    ### Firstly the mirror surface (a circle) is broken up into n_point segments. The area of each segment is calculated
    ### and is converted to a fraction of the total area. Additionally, a mirror separation correction is calculated at
    ### n_points - 1 equally spaced locations along the mirror axis (radially outwards). The transmittance and
    ### reflectance is calculated for each point and are scaled according to the fractional area of the segment.
    diameter = 43e-3  # mirror diameter
    # mirror_height: Maximum height difference between mirror center and edges
    R = mirror_height / 2 + (diameter ** 2) / (8 * mirror_height)  # radius of mirror curvature

    n_points = int(n_points) #points must be an integer
    if n_points > 1:
        r_area = np.linspace(0, diameter / 2, n_points)  # radii used for area calculations
        r_eval = r_area + np.diff(r_area)[0] / 2  # radii at which the mirror separation difference is calculated
        r_area = np.delete(r_area, 0)  # Since the first radius is 0, the area is also 0 and is therefore omitted
        r_eval = np.delete(r_eval,-1)  # The evaluation points lie in the middle between r_area, but the final r_eval is outside the mirror and is therefore deleted
        area = []
        diff = []
        for i in range(n_points - 1):
            diff.append(mirror_dist_diff(r_eval[i], R))
            if i == 0:
                area.append(np.pi * r_area[i] ** 2)  # area of circle
            else:
                area.append(np.pi * (r_area[i] ** 2 - r_area[i - 1] ** 2))  # area of ring
        total_area = sum(area)
        mirror_fractions = np.array(area) / total_area
    else:
        mirror_fractions = [1]
        diff = [0]

    # The blocks refer to:
    # block1 - antireflective coating left half
    # block2_1: mirror coating left half
    # block2_2: mirror coating right half
    # block3: antireflective coating right half

    #list containing functions for calculating ior for each layer in the antireflective coating
    ar_functions = [n_air, n_ThF4, n_ZnSe, n_ThF4, n_ZnSe, n_ThF4, n_ZnSe] #Also contains the layers immediately to the left and right of the antireflecctive coating
    n_block1 = [] #list of refractive indices
    d_block1 = np.array([np.inf, 4350, 250, 940, 500, 340, np.inf]) * 1e-9 #layer thicknesses
    Z_block1 = np.array([0, 0, 0, 0, 0, 0]) * 1e-9 #list of interface rms heights
    for func in ar_functions:
        n_block1.append(func(lams))
    n_block1 = np.array(n_block1)
    n_block3 = n_block1[::-1] #the lists are mirrored to match the other half of the FPI
    d_block3 = d_block1[::-1]
    Z_block3 = Z_block1[::-1]

    # Now do the same, but for the mirror coatings (excluding the air gap)
    mirror_functions = [n_ZnSe, n_Ge, n_ZnS, n_ThF4, n_ZnS, n_Ge, n_air]
    n_block2_1 = []
    d_block2_1 = np.array([np.inf, 1255, 20, 1785, 20, 510, np.inf]) * 1e-9
    Z_block2_1 = np.array([0, 0, 0, 0, 0, 0]) * 1e-9
    for func in mirror_functions:
        n_block2_1.append(func(lams))
    n_block2_1 = np.array(n_block2_1)
    n_block2_2 = n_block2_1[::-1]
    d_block2_2 = d_block2_1[::-1]
    Z_block2_2 = Z_block2_1[::-1]

    #angle in each layer from snell's law
    if angle != 0:
        angles_block1 = []
        angles_block1.append(np.ones_like(lams)*angle)
        for i in range(n_block1.shape[0]-1):
            angles_block1.append(np.arcsin(np.sin(angles_block1[-1])*np.real(n_block1[i, :])/np.real(n_block1[i+1, :])))
        angles_block2_1 = []
        angles_block2_1.append(angles_block1[-1])
        for i in range(len(n_block2_1)-1):
            angles_block2_1.append(np.arcsin(np.sin(angles_block2_1[-1])*np.real(n_block2_1[i, :])/np.real(n_block2_1[i+1, :])))
        angles_block2_2 = []
        angles_block2_2.append(angles_block2_1[-1])
        for i in range(len(n_block2_2)-1):
            angles_block2_2.append(np.arcsin(np.sin(angles_block2_2[-1])*np.real(n_block2_2[i, :])/np.real(n_block2_2[i+1, :])))
        angles_block3 = []
        angles_block3.append(angles_block2_2[-1])
        for i in range(len(n_block3)-1):
            angles_block3.append(np.arcsin(np.sin(angles_block3[-1])*np.real(n_block3[i, :])/np.real(n_block3[i+1, :])))
        angles_block1 = np.array(angles_block1)
        angles_block2_1 = np.array(angles_block2_1)
        angles_block2_2 = np.array(angles_block2_2)
        angles_block3 = np.array(angles_block3)
    else:
        angles_block1 = np.zeros_like(n_block1)
        angles_block2_1 = np.zeros_like(n_block2_1)
        angles_block2_2 = np.zeros_like(n_block2_2)
        angles_block3 = np.zeros_like(n_block3)


    #Calculate the index of refraction for ZnSe and air for all relevant wavelengths
    ns_ZnSe = n_ZnSe(lams)
    ns_air = n_air(lams)

    #Matrices for containing the transmittance and reflectance 
    transmittance_matrix = np.zeros([len(m_seps), len(lams)])
    reflectance_matrix = np.zeros([len(m_seps), len(lams)])

    #For each wavelength calculate all the relevant transfer matrices. These are converted to their aboslute counterparts
    #to accomedate for the incoherent ZnSe layer
    #Do to speed, the calculations are split up depending on whether the incidence is normal or not
    if angle == 0: #normal insicense
        for i, lam in enumerate(lams):
            T1 = transfer_matrix(n_block1[:,i], d_block1, Z_block1, lam)
            T1_abs = abs_transfer_matrix(T1)
            T2_1 = transfer_matrix(n_block2_1[:,i], d_block2_1, Z_block2_1, lam)
            T2_2 = transfer_matrix(n_block2_2[:,i], d_block2_2, Z_block2_2, lam)
            T3 = transfer_matrix(n_block3[:,i], d_block3, Z_block3, lam)
            T3_abs = abs_transfer_matrix(T3)
            P_ZnSe_abs = abs(p_matrix(ns_ZnSe[i], 5e-3, lam))**2
            T1_ZnSe_abs = T1_abs@P_ZnSe_abs
            T3_ZnSe_abs = P_ZnSe_abs@T3_abs

            #Now calculate the effective transfer matrix for all mirror separations. The results are converted to transmittance and reflectance.
            for j, m_sep in enumerate(m_seps):
                T = 0
                R = 0
                for d, frac in zip(diff, mirror_fractions):
                    P_air = p_matrix(ns_air[i], m_sep + d, lam)
                    T2 = T2_1 @ P_air @ T2_2
                    T2_abs = abs_transfer_matrix(T2)
                    T_combined = T1_ZnSe_abs @ T2_abs @ T3_ZnSe_abs
                    T += 1 / T_combined[0, 0] * frac
                    R += T_combined[1,0]/T_combined[0,0] * frac
                transmittance_matrix[j,i] = T
                reflectance_matrix[j,i] = R
    else:
        for i, lam in enumerate(lams):
            T1 = transfer_matrix_angular(n_block1[:, i], d_block1/np.cos(angles_block1[:,i]), angles_block1[:,i], fraction_s_pol, Z_block1, lam)
            T1_abs = abs_transfer_matrix(T1)
            T2_1 = transfer_matrix_angular(n_block2_1[:, i], d_block2_1/np.cos(angles_block2_1[:,i]), angles_block2_1[:,i], fraction_s_pol, Z_block2_1, lam)
            T2_2 = transfer_matrix_angular(n_block2_2[:, i], d_block2_2/np.cos(angles_block2_2[:,i]), angles_block2_2[:,i], fraction_s_pol, Z_block2_2, lam)
            T3 = transfer_matrix_angular(n_block3[:, i], d_block3/np.cos(angles_block3[:,i]), angles_block3[:,i], fraction_s_pol, Z_block3, lam)
            T3_abs = abs_transfer_matrix(T3)
            P_ZnSe_abs1 = abs(p_matrix(ns_ZnSe[i], 5e-3/np.cos(angles_block1[-1,i]), lam)) ** 2
            T1_ZnSe_abs = T1_abs @ P_ZnSe_abs1
            P_ZnSe_abs2 = abs(p_matrix(ns_ZnSe[i], 5e-3/np.cos(angles_block2_2[-1,i]), lam)) ** 2
            T3_ZnSe_abs = P_ZnSe_abs2 @ T3_abs

            # Now calculate the effective transfer matrix for all mirror separations. The results are converted to transmittance and reflectance.
            for j, m_sep in enumerate(m_seps):
                T = 0
                R = 0
                for d, frac in zip(diff, mirror_fractions):
                    P_air = p_matrix(ns_air[i], (m_sep + d)/np.cos(angles_block2_1[-1,i]), lam)
                    T2 = T2_1 @ P_air @ T2_2
                    T2_abs = abs_transfer_matrix(T2)
                    T_combined = T1_ZnSe_abs @ T2_abs @ T3_ZnSe_abs
                    # T_combined = T2
                    n_ratio = np.real(ns_air[i] * np.cos(angles_block3[-1, i])) / np.real(ns_air[i] * np.cos(angles_block1[0, i]))
                    T += 1 / T_combined[0, 0] * n_ratio * frac
                    R += T_combined[1, 0] / T_combined[0, 0] * frac
                transmittance_matrix[j, i] = T
                reflectance_matrix[j, i] = R
    return transmittance_matrix, reflectance_matrix

# function for calculating the transfer matrix of an entire stack of layers
def transfer_matrix(n_stack, d_stack, Z_stack, lam):
    T_matrix = t_matrix(n_stack[0], n_stack[1], Z_stack[0], lam)
    for j in np.arange(1, len(n_stack) - 1):
        T_matrix = T_matrix @ p_matrix(n_stack[j], d_stack[j], lam) @ t_matrix(n_stack[j], n_stack[j+1], Z_stack[j], lam)
    return T_matrix

def transfer_matrix_angular(n_stack, d_stack, angle_stack, fraction, Z_stack,  lam):
    T_matrix = t_matrix_angular(n_stack[0], n_stack[1], angle_stack[0], angle_stack[1], fraction, Z_stack[0], lam)
    for j in np.arange(1, len(n_stack) - 1):
        T_matrix = T_matrix @ p_matrix(n_stack[j], d_stack[j]/np.cos(angle_stack[j]), lam) @ t_matrix_angular(n_stack[j], n_stack[j+1], angle_stack[j], angle_stack[j+1], fraction, Z_stack[j], lam)
    return T_matrix

# function for converting a transfer matrix to absolute values
def abs_transfer_matrix(transfermatrix):
    t = 1 / transfermatrix[0, 0]
    t_prime = (transfermatrix[0, 0] * transfermatrix[1, 1] - transfermatrix[0, 1] * transfermatrix[1, 0]) / transfermatrix[0, 0]
    r = transfermatrix[1, 0] / transfermatrix[0, 0]
    r_prime = - transfermatrix[0, 1] / transfermatrix[0, 0]
    return 1 / (abs(t) ** 2) * np.array([[1, -abs(r_prime) ** 2], [abs(r) ** 2, abs(t * t_prime) ** 2 - abs(r * r_prime) ** 2]])


# function for calculating the transmission matrix
def t_matrix(n1, n2, Z=0, lam = 1):
    if Z == 0: # measurable speed up, if the exponents do not have to be calculated in case of no roughness.
        a = 1
        b = 1
        c = 1
    else:
        s = 2*np.pi*Z
        a = np.exp(-2*(s*n1/lam)**2)
        b = np.exp(-2*(s*n2/lam)**2)
        c = np.exp(-0.5 * ((s*n2/lam)**2 * (n1 - n2)**2))
    r = a*reflectance(n1, n2)
    r_prime = b*reflectance(n2, n1)
    t = c*transmittance(n1, n2)
    t_prime = c*transmittance(n2, n1)
    matrix = np.array([[1, -r_prime], [r, t*t_prime-r*r_prime]])
    return (1/t) * matrix

def t_matrix_angular(n1, n2, theta1, theta2, fraction, Z=0, lam = 1):
    if Z == 0: # measurable speed up, if the exponents do not have to be calculated in case of no roughness.
        a = 1
        b = 1
        c = 1
    else:
        s = 2*np.pi*Z
        a = np.exp(-2*(s*n1/lam)**2)
        b = np.exp(-2*(s*n2/lam)**2)
        c = np.exp(-0.5 * ((s*n2/lam)**2 * (n1 - n2)**2))
    r = a*reflectance_angular(n1, n2, theta1, theta2, fraction)
    r_prime = b*reflectance_angular(n2, n1, theta2, theta1, fraction)
    t = c*transmittance_angular(n1, n2, theta1, theta2, fraction)
    t_prime = c*transmittance_angular(n2, n1, theta2, theta1, fraction)
    matrix = np.array([[1, -r_prime], [r, t*t_prime-r*r_prime]])
    return (1/t) * matrix

# calculate the phase matrix
def p_matrix(n, d, lam):
    P = np.zeros([2,2], dtype=np.complex_)
    P[0, 0] = np.exp(1j * n * 2 * np.pi * d / lam)
    P[1, 1] = np.exp(-1j * n * 2 * np.pi * d / lam)
    return P

# calculate the reflectance based on refractive indices
def reflectance(n1, n2):
    return (n1 - n2)/(n1 + n2)

# calculate the reflectance based on refractive indices and angles
def reflectance_angular(n1, n2, theta1, theta2, fraction):
    rs = (n1*np.cos(theta1) - n2*np.cos(theta2))/(n1*np.cos(theta1) + n2*np.cos(theta2))
    rp = -(n2*np.cos(theta1) - n1*np.cos(theta2))/(n2*np.cos(theta1) + n1*np.cos(theta2)) ##### NOTICE THE CHANGE OF SIGN FOR rp - SEE STEVEN BYRNES #####
    return fraction*rs + (1-fraction)*rp

# calculate the transmittance based on refractive indices
def transmittance(n1, n2):
    return 2*n1/(n1 + n2)

# calculate the transmittance based on refractive indices and angles
def transmittance_angular(n1, n2, theta1, theta2, fraction):
    ts = 2*n1*np.cos(theta1)/(n1*np.cos(theta1) + n2*np.cos(theta2))
    tp = 2*n1*np.cos(theta1)/(n2*np.cos(theta1) + n1*np.cos(theta2))
    return fraction*ts + (1-fraction)*tp

# calculate phase gained from traveling in a medium
def phase(n, d, lam):
    return np.exp(1j * n * 2 * np.pi * d / lam)

# function for calculating the deviation from perfectly flat mirror at radius r from mirror center.
def mirror_dist_diff(r, R):
    return -2 * (0.5 * (2 * R - np.sqrt(4 * R ** 2 - (2 * r) ** 2)))

######## Functions for calculating the refractive indices of different materials ########

def n_air(lams):
    return np.ones_like(lams, dtype=np.complex_)

def n_ThF4(lams):
    # Handbook of Optical Constants of Solids II, 1998, page 1051
    lams = lams * 1e6
    k = 0.00189 - 0.00015 * lams + 0.00001 * lams ** 2
    n = 1.118 + 2.46 / lams - 2.98 / (lams ** 2)  # - ThF4_k_interp*1j
    return n - k * 1j

def n_ZnSe(lams):
    # Handbook of Optical Constants of Solids II, page 737
    lams = lams * 1e6
    n = np.sqrt(4 + 1.9 * lams ** 2 / (lams ** 2 - 0.113)) - 0j
    return n

def n_ZnS(lams):
    # Handbook of Optical Constants of Solids I, page 600
    w = (1 / lams) * 1e-2
    wL = 352  # cm^-1
    wT = 282  # cm^-1
    T = 6.77  # cm^-1
    eps_inf = 5.7
    n = np.sqrt(eps_inf * (1 + (wL ** 2 - wT ** 2) / (wT ** 2 - w ** 2 + T * w * 1j)))
    return np.real(n) + np.imag(n)*1j

def n_Ge(lams):
    temperature = 293.15
    # Handbook of Optical Constants of Solids I, page 465 - for bulk
    lams = lams * 1e6
    # A = -6.04e-3 * temperature + 11.05128
    # B = 9.295e-3 * temperature + 4.00536
    # C = -5.392e-4 * temperature + 0.599034
    # D = 4.151e-4 * temperature + 0.09145
    # E = 1.51408 * temperature + 3426.5
    # n1 = np.sqrt(A + (B * lams ** 2) / (lams ** 2 - C) + (D * lams ** 2) / (lams ** 2 - E))

    # https://doi.org/10.1016/j.mssp.2018.04.019 - for thin film
    A = 4.1463
    B = 0.57268
    C = 0.087329
    n = A + B / (lams ** 2) + C / (lams ** 4)

    # n = 0.5*(n1 + n2)

    alpha = 0.064314
    Eg = 0.77285
    Eu = 0.142
    k = alpha * np.exp((1.24 / lams - Eg) / Eu) # also from https://doi.org/10.1016/j.mssp.2018.04.019
    return n - k * 1j

