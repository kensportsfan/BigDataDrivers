import numpy as np
from scipy import special

#systems of normalizing data

#gets the binarization function for a given threshold
def getBinarizeFunc(threshold):
    #make all data one or zero, depending on whether it is >= the threshold
    def binarize(data):
        return np.array([1 if item >= threshold else 0 for item in data])
    return binarize



#make all data range from 0 to 1, scaled to the max value
def linearScale(data):
    high = float(max(data))
    return np.array([item/high for item in data])

#gets the chi squared cumulative probability function for a given dimension
#square inputs is for squaring the data before placing it in the chi square dist
#(mahalanobis dist ** 2 is chi squared distributed)
def getChiSquareFunc(dimension, squareInputs=True):
    def cumChiSquare(data):
        if squareInputs:
            data = np.array([item ** 2 for item in data])
        return np.array([special.chdtr(dimension, item) for item in data])
    return cumChiSquare

#just returns the data. cute!
def doNothing(data):
    return data
