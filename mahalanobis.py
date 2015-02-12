#gets Mahalanobis distances for spy and unlabeled data

import numpy as np
from sklearn.covariance import MinCovDet

#both arguments must be 2D numpy arrays with each row
#containing an observation

#returns distnaces in two single dimensional arrays
#first the unlabeled, then the spy
def getDistances(unlabeled, spy):
    X = np.append(unlabeled, spy, axis=0)
    robust_cov = MinCovDet().fit(X)
    unlabeledDists = robust_cov.mahalanobis(unlabeled)
    spyDists = robust_cov.mahalanobis(spy)
    return unlabeledDists, spyDists
