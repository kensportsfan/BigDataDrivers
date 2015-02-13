import features
import getcsv
import numpy as np

def importGroup(foldername, feats, count=200):
    return np.array(map(lambda x: features.selectFeatures(x,feats),
        getcsv.getGroup(foldername, count=count)))
