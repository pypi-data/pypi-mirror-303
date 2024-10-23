import numpy as np

# This function calculates the fraction of the energy contained below wavelength, lam, compared to the total energy of a black body emitter at a given temperature. 
# This is done without numerical integration using the method proposed in  https://www.ijee.ie/articles/Vol20-6/IJEE1557.pdf
def bb_frac_lam(lam, temperature):
    h = 6.62607004e-34 #[m2 kg / s]
    c = 299792458 #[m / s]
    kB = 1.380649e-23 #[J/K]
    C2 = h*c/kB
    z = C2/(lam*temperature)
    N = 5
    F = 0
    for i in np.arange(1,N+1):
        ci = z**3/i + 3*z**2/(i**2) + 6*z/(i**3) + 6/(i**4)
        F += ci*np.exp(-i*z)
    return 15*F/(np.pi**4)

# This function uses bb_frac_lam to calculate a spectrum of exitances. The input wavelengths, lams, are the center wavelengths of each 'bin' within wich the exitance is calculated.
# The black body temperature is also supplied. 
def bb_exitance_lam(lams, temperature):
    #lams are the central wavelengths of each 'bin'. A new wavelength axis is generated, where all points are
    #shifted half a wavelength step to form the intervals in which the black body fractions are calculated
    temp_lams = np.zeros(len(lams)+1)
    dlams = np.diff(lams)
    temp_lams[1:-1] = lams[:-1] + dlams/2
    temp_lams[0] = lams[0] - dlams[0]/2
    temp_lams[-1] = lams[-1] + dlams[-1]/2

    bb_fracs = np.zeros_like(temp_lams)
    for i in range(len(temp_lams)):
        bb_fracs[i] = bb_frac_lam(temp_lams[i], temperature)
        
    h = 6.62607004e-34 #[m2 kg / s]
    c = 299792458 #[m / s]
    kB = 1.380649e-23 #[J/K]
    sigma = 2*np.pi**5*kB**4/(15*c**2*h**3)
    return abs(np.diff(bb_fracs))*(sigma*temperature**4) #[W/m^2] for each bin. Smaller bins of course lead to smaller exitance in given interval


# The following functions are the same as previously, but rewritten to work with wavenumbers instead. 

def bb_frac_k(k, temperature):
    h = 6.62607004e-34 #[m2 kg / s]
    c = 299792458 #[m / s]
    kB = 1.380649e-23 #[J/K]
    C2 = h*c/kB
    C1 = h*c**2
    z = k*C2/T
    N = 5
    F = 0
    for n in np.arange(1,N+1):
        F += - np.exp(-n*z) * (z**3/n + 3*z**2/(n**2) + 6*z/(n**3) + 6/(n**4)) + 6/(n**4)
    return F*2*np.pi*C1/(sigma*C2**4)

def bb_exitance_k(wvnbs, temperature):
    #wvnbs are the central wavenumber of each 'bin'. A new wavenumber axis is generated, where all points are
    #shifted half a wavenumber step to form the intervals in which the black body fractions are calculated
    temp_wvnbs = np.zeros(len(wvnbs)+1)
    dwvnbs = np.diff(wvnbs)
    temp_wvnbs[1:-1] = wvnbs[:-1] + dwvnbs/2
    temp_wvnbs[0] = wvnbs[0] - dwvnbs[0]/2
    temp_wvnbs[-1] = wvnbs[-1] + dwvnbs[-1]/2

    bb_fracs = np.zeros_like(temp_wvnbs)
    for i in range(len(temp_wvnbs)):
        bb_fracs[i] = bb_frac_k(temp_wvnbs[i], temperature)
        
    h = 6.62607004e-34 #[m2 kg / s]
    c = 299792458 #[m / s]
    kB = 1.380649e-23 #[J/K]
    sigma = 2*np.pi**5*kB**4/(15*c**2*h**3)
    return abs(np.diff(bb_fracs))*(sigma*temperature**4) #[W/m^2] for each bin. Smaller bins of course lead to smaller exitance in given interval
