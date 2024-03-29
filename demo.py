import tester
import mahalanobis
import normalize
import numpy as np
import random

#simple demo to evaluate classifier using PU eval metric (ranksum ratio)
def demoPU(n_samples=125, n_outliers=10, n_features=2, pollution=15,
           norm=normalize.linearScale, data=None):
    if not data:
        X, outliers, key = demoData(n_samples=n_samples, n_outliers=n_outliers,
                                    n_features=n_features, pollution=pollution)
    else:
        X, outliers, key = data
        
    result = tester.testPUClassifier(mahalanobis.getDistances, X, outliers, norm)

    print(result)
    return result

# simple demo to evaluate classifier with known data
# returns area under ROC
def demoSup(n_samples=125, n_outliers=10, n_features=2, pollution=15,
            norm=normalize.linearScale, data=None, showGraph=False,
            title='Spring Break'):
    if not data:
        X, outliers, key = demoData(n_samples=n_samples, n_outliers=n_outliers,
                                    n_features=n_features, pollution=pollution)
    else:
        X, outliers, key = data

    X = np.append(X, outliers, axis=0)
        
    result = tester.testSupervisedClassifier(mahalanobis.getDistances, X, key, norm,
                                             showGraph=showGraph, title=title)

    print(result)
    return result

# simple demo to check performance of PU evaluation metric
# returns a dict containing PU (ranksum ratio) score and Sup score (AUC)
def demoAUCcomp(n_samples=125, n_outliers=10, n_features=2, pollution=15,
           norm=normalize.linearScale, data=None, showGraph=False):
    if not data:
        data = demoData(n_samples=n_samples, n_outliers=n_outliers,
                                    n_features=n_features, pollution=pollution)
    print "starting PU"
    pu = demoPU(n_samples=n_samples, n_outliers=n_outliers, n_features=n_features,
           pollution=pollution, norm=norm, data=data)
    print "starting SUP"
    sup = demoSup(n_samples=n_samples, n_outliers=n_outliers, n_features=n_features,
           pollution=pollution, norm=norm, data=data,showGraph=showGraph)
    return {"pu":pu,"sup":sup}
    
#adapted from scikit-learn example
#http://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#example-covariance-plot-mahalanobis-distances-py
def demoData(n_samples=125, n_outliers=10, n_features=2, pollution=15, outlierMultiplier=7.):
    # generate data
    gen_cov = np.eye(n_features)
    gen_cov[0, 0] = 2.
    X = np.dot(np.random.randn(n_samples, n_features), gen_cov)

    #generate outliers
    outliers_cov = np.eye(n_features)
    outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = float(outlierMultiplier)
    outliers = np.dot(np.random.randn(n_outliers*10, n_features), outliers_cov)

    contaminants = []
    #pollute
    for x in xrange(pollution):
        index = random.randint(0,len(X)-1) 
        contaminants.append(index)
        X[index] = outliers[random.randint(0,len(outliers)-1)]

    contaminants = set(contaminants)

    key = []

    for i in xrange(len(X)+n_outliers):
        if i in contaminants or i >= len(X):
            key.append(1)
        else:
            key.append(0)

    return X, outliers[:n_outliers], key
