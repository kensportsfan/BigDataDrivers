import features
import getcsv
import numpy as np
import sav

# feats must be in format of a list of (function name, version, arg list)
def importGroup(foldername, feats, count=200):
    
        
    #return np.array(map(lambda x: features.selectFeatures(x,feats),
    #    getcsv.getGroup(foldername, count=count)))

def importDrive(filename, feats):
    values = readSav(filename)
    copy = feats[:]
    for feat in feats:
        
