import features
import getcsv
import numpy as np
import sav

# feats must be in format of a list of (function name, version, arg set)
def importGroup(folderNum, feats, count=200):
    
        
    #return np.array(map(lambda x: features.selectFeatures(x,feats),
    #    getcsv.getGroup(foldername, count=count)))


def importDrive(folderNum, fileNum, feats):
    cachedFeats = getCachedFeatures(folderNum, fileNum)
    copy = feats[:]
    featList = []
    for feat in feats:
        for cachedFeat, value in cachedFeats:
            if feat == cachedFeat:
                print "holy shit"
                featList.append(value)
            else:
                
                
            
        
