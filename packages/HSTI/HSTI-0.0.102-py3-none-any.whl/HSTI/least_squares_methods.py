import numpy as np
from fnnls import fnnls
from sklearn.isotonic import IsotonicRegression
import numpy.matlib
#########################################################################################################################
#########################################################################################################################
###################### Alternating Least Squares, which returns spectral and contribution profiles ######################
#########################################################################################################################
#########################################################################################################################

## The input matrix is given by X represents spectral measurements. Each row represents a single spectrum.
## X is factorized into a matrix of contributions and a matrix of spectra as well as the error not captured by the model.
## A number of constraints can be set. These include nonnegativity for both spectra and contributions,
## closure can be imposed on the contribution profiles meaning that they will sum to 1.
## Finally, unimodality can be imposed for either the contribution or the spectral profiles such that
## each solution/spectrum only have a single maximum.
## The ALS algorithm requires an initial guess which can be either a spectral profile or contribution profile.
## Two methods are used for this: calculate_ALS_from_spectrum() and calculate_ALS_from_contribution().
## The initial guess determines the number of components, the model will search for in its solution.


class ALS:
# https://doi.org/10.1002/(SICI)1099-128X(199807/08)12:4<223::AID-CEM511>3.0.CO;2-2
# htals.m from hypertools

    def __init__(self):
        self.spectra = 0
        self.contributions = 0
        self.error = []
        self.X = 0
        self.X_hat = 0

## Notes used for previous versions of the code
### hypertools closure:     # self.contributions[j,:] = fnnls(self.spectra.T@self.spectra, self.spectra.T@self.X[j,:])[0] #Taken from hypertools
### hypertools closure:     # self.spectra[j,:] = fnnls(self.contributions.T@self.contributions, self.contributions.T@self.X[:,j])[0] #Taken from hypertools
    def calculate_ALS_from_spectrum(self, matrix, spectra, closure = False, nonnegativity_c = False, nonnegativity_s = False, unimodality_s = False, contrast_weight = 0.00, thresh = 1e-8, max_it = 50):
        self.spectra = np.copy(spectra)
        self.X = np.copy(matrix)
        self.it = 0
        self.contributions = np.zeros([matrix.shape[0], spectra.shape[1]])
        self.temp_specs = []
        for i in range(max_it):
            self.it += 1
            self.temp_specs.append(np.copy(self.spectra))

            self.spectra = (1 - contrast_weight)*self.spectra + contrast_weight*np.matlib.repmat(np.mean(self.spectra, axis = 1 )[:,np.newaxis],1,self.spectra.shape[1])

            if nonnegativity_c:
                for j in range(self.contributions.shape[0]):
                    self.contributions[j,:] = fnnls(self.spectra, self.X[j,:])[0] #self.X[j,:][:,np.newaxis] transforms j'th row of X into column vector


            if closure:
                for j in range(self.contributions.shape[0]):
                    if np.sum(self.contributions[j,:]) > 0:
                        self.contributions[j,:] = self.contributions[j,:]/np.sum(self.contributions[j,:])
                    else:
                        self.contributions[j,:] = np.zeros(self.contributions.shape[1])


            if (closure == False) and (nonnegativity_c == False) and (unimodality_s == False):
                # self.contributions = self.X@self.spectra@np.linalg.pinv(self.spectra.T@self.spectra)
                self.contributions = self.X@np.linalg.pinv(self.spectra.T)


            if nonnegativity_s:
                for j in range(self.spectra.shape[0]):
                    self.spectra[j,:] = fnnls(self.contributions, self.X[:,j])[0]


            if unimodality_s: #https://doi.org/10.1002/(SICI)1099-128X(199807/08)12:4<223::AID-CEM511>3.0.CO;2-2
                ir_incr = IsotonicRegression(increasing=True)
                ir_decr = IsotonicRegression(increasing=False)
                idx = np.arange(self.spectra.shape[0])
                self.c = []
                for j in range(self.spectra.shape[1]): #Loop through each spectrum
                    self.c.append(np.zeros([self.spectra.shape[0],self.spectra.shape[0]]))
                    self.c_fit = []
                    for k in range(self.spectra.shape[0]): #Loop through each possible position of maximum
                        if k == 0:
                            self.c[j][k,k] = self.spectra[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.spectra[k+1:,j])
                        elif k == self.spectra.shape[0]-1:
                            self.c[j][:-1,k] = ir_incr.fit_transform(idx[:-1], self.spectra[:-1,j])
                            self.c[j][k,k] = self.spectra[k,j]
                        else:
                            self.c[j][0:k,k] = ir_incr.fit_transform(idx[0:k], self.spectra[0:k,j])
                            self.c[j][k,k] = self.spectra[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.spectra[k+1:,j])
                        if (self.c[j][k,k] == np.max(self.c[j][:,k])) and (np.max(self.c[j][:,k]) > 0):
                            self.c_fit.append(self.c[j][:,k])
                    #Find best position of maximum
                    best_fit_err = np.inf
                    best_fit = np.zeros(self.spectra.shape[0])
                    for fit in self.c_fit:
                        if np.linalg.norm(self.spectra[:,j] - fit) < best_fit_err:
                            best_fit = fit
                            best_fit_err = np.linalg.norm(self.spectra[:,j] - fit)
                    self.spectra[:,j] = best_fit


            if (nonnegativity_s == False) and (unimodality_s == False):
                # self.spectra = self.X.T@self.contributions@np.linalg.pinv(self.contributions.T@self.contributions)
                self.spectra = (np.linalg.pinv(self.contributions)@self.X).T

            if np.linalg.norm(self.spectra) > 0:
                self.spectra = self.spectra/np.linalg.norm(self.spectra)
            else:
                self.spectra = np.zeros_like(self.spectra)
            X_old = self.X
            self.X = self.contributions@self.spectra.T
            self.error.append(matrix - self.X)
            if np.linalg.norm(X_old - self.X) < thresh:
                break
            elif i == max_it-1:
                print("Maximum number of iterations reached")

    def calculate_ALS_from_contribution(self, matrix, contributions, closure = False, nonnegativity_c = False, nonnegativity_s = False, unimodality_c = False, thresh = 1e-8, max_it = 50):
        self.contributions = np.copy(contributions)
        self.X = np.copy(matrix)
        self.it = 0
        self.spectra = np.zeros([matrix.shape[1], contributions.shape[1]])
        for i in range(max_it):
            self.it += 1


            if nonnegativity_s:
                for j in range(self.spectra.shape[0]):
                    self.spectra[j,:] = fnnls(self.contributions, self.X[:,j])[0]


            if unimodality_c: #https://doi.org/10.1002/(SICI)1099-128X(199807/08)12:4<223::AID-CEM511>3.0.CO;2-2
                ir_incr = IsotonicRegression(increasing=True)
                ir_decr = IsotonicRegression(increasing=False)
                idx = np.arange(self.contributions.shape[0])
                self.c = []
                for j in range(self.contributions.shape[1]): #Loop through each spectrum
                    self.c.append(np.zeros([self.contributions.shape[0],self.contributions.shape[0]]))
                    self.c_fit = []
                    for k in range(self.contributions.shape[0]): #Loop through each possible position of maximum
                        if k == 0:
                            self.c[j][k,k] = self.contributions[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.contributions[k+1:,j])
                        elif k == self.contributions.shape[0]-1:
                            self.c[j][:-1,k] = ir_incr.fit_transform(idx[:-1], self.contributions[:-1,j])
                            self.c[j][k,k] = self.contributions[k,j]
                        else:
                            self.c[j][0:k,k] = ir_incr.fit_transform(idx[0:k], self.contributions[0:k,j])
                            self.c[j][k,k] = self.contributions[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.contributions[k+1:,j])
                        if (self.c[j][k,k] == np.max(self.c[j][:,k])) and (np.max(self.c[j][:,k]) > 0):
                            self.c_fit.append(self.c[j][:,k])
                    #Find best position of maximum
                    best_fit_err = np.inf
                    best_fit = np.zeros(self.contributions.shape[0])
                    for fit in self.c_fit:
                        if np.linalg.norm(self.contributions[:,j] - fit) < best_fit_err:
                            best_fit = fit
                            best_fit_err = np.linalg.norm(self.contributions[:,j] - fit)
                    self.contributions[:,j] = best_fit


            if (nonnegativity_s == False) and (unimodality_s == False):
                self.spectra = self.X.T@self.contributions@np.linalg.pinv(self.contributions.T@self.contributions)

            if np.linalg.norm(self.spectra) > 0:
                self.spectra = self.spectra/np.linalg.norm(self.spectra)
            else:
                self.spectra = np.zeros_like(self.spectra)


            if nonnegativity_c:
                for j in range(self.contributions.shape[0]):
                    self.contributions[j,:] = fnnls(self.spectra, self.X[j,:])[0] #self.X[j,:][:,np.newaxis] transforms j'th row of X into column vector


            if closure:
                for j in range(self.contributions.shape[0]):
                    if np.sum(self.contributions[j,:]) > 0:
                        self.contributions[j,:] = self.contributions[j,:]/np.sum(self.contributions[j,:])
                    else:
                        self.contributions[j,:] = np.zeros(self.contributions.shape[1])


            if unimodality_c: #https://doi.org/10.1002/(SICI)1099-128X(199807/08)12:4<223::AID-CEM511>3.0.CO;2-2
                ir_incr = IsotonicRegression(increasing=True)
                ir_decr = IsotonicRegression(increasing=False)
                idx = np.arange(self.contributions.shape[0])
                self.c = []
                for j in range(self.contributions.shape[1]): #Loop through each spectrum
                    self.c.append(np.zeros([self.contributions.shape[0],self.contributions.shape[0]]))
                    self.c_fit = []
                    for k in range(self.contributions.shape[0]): #Loop through each possible position of maximum
                        if k == 0:
                            self.c[j][k,k] = self.contributions[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.contributions[k+1:,j])
                        elif k == self.contributions.shape[0]-1:
                            self.c[j][:-1,k] = ir_incr.fit_transform(idx[:-1], self.contributions[:-1,j])
                            self.c[j][k,k] = self.contributions[k,j]
                        else:
                            self.c[j][0:k,k] = ir_incr.fit_transform(idx[0:k], self.contributions[0:k,j])
                            self.c[j][k,k] = self.contributions[k,j]
                            self.c[j][k+1:,k] = ir_decr.fit_transform(idx[k+1:], self.contributions[k+1:,j])
                        if (self.c[j][k,k] == np.max(self.c[j][:,k])) and (np.max(self.c[j][:,k]) > 0):
                            self.c_fit.append(self.c[j][:,k])
                    #Find best position of maximum
                    best_fit_err = np.inf
                    best_fit = np.zeros(self.contributions.shape[0])
                    for fit in self.c_fit:
                        if np.linalg.norm(self.contributions[:,j] - fit) < best_fit_err:
                            best_fit = fit
                            best_fit_err = np.linalg.norm(self.contributions[:,j] - fit)
                    self.contributions[:,j] = best_fit


            if (closure == False) and (nonnegativity_c == False) and (unimodality_c == False):
                self.contributions = self.X@self.spectra@np.linalg.pinv(self.spectra.T@self.spectra)

            X_old = self.X
            self.X = self.contributions@self.spectra.T
            self.error.append(matrix - self.contributions@self.spectra.T)
            if np.linalg.norm(X_old - self.X) < thresh:
                break
            elif i == max_it-1:
                print("Maximum number of iterations reached")


########################################################################################################################
########################################################################################################################
############################################## Generalized Least Squares  ##############################################
########################################################################################################################
########################################################################################################################


class GLS:
    def __init__(self):
        self.spectra = 0
        self.contributions = 0
        self.error = 0
        self.X = 0
        self.X_hat = 0
        self.lam = 0

## Calculate the contributions of target and clutter. The data matrix is structured
## to have each sample represented by a row with each column representing a single wavelength.
## A target spectrum is supplied, and clutter is then defined as the mean of all the data.
## The data covariance matrix is used to deweigh the most prominent directions within the data
## such that the target stands out more easily. For this deweighting, the data is regularized.
## This is done by adding a constant value to the eigen values of the clutter covariance matrix.
## This value is determined by the regularization_parameter

## The contributions contain two vectors. The first describe the contribution of the targeted
## while the second describe the contribution of the clutter.
    def calculate_contributions(self, matrix, target, clutter = None, regularization_parameter = 1e-5):
        self.X = np.copy(matrix)
        self.target = np.copy(target)
        if clutter == None:
            clutter = np.mean(self.X, axis = 0)[:,np.newaxis]
        self.spectra = np.c_[self.target, clutter]
        self.lam = regularization_parameter
        self.weights = np.cov(self.X.T)

        U, s, Vh = np.linalg.svd(self.weights, full_matrices = False)
        S = np.diag(s)
        D = np.eye(S.shape[0])*self.lam

        self.weights_inv = Vh.T@np.linalg.inv(S+D)@U.T

        self.contributions = np.linalg.inv(self.spectra.T@self.weights_inv@self.spectra)@self.spectra.T@self.weights_inv@self.X.T
        self.X_hat = self.contributions.T@self.spectra.T
        self.error = self.X - self.X_hat
