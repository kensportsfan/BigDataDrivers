import features
import getcsv
import numpy as np
import sav
import cacheFeature as cf

# feats must be in format of a list of (function name, version, arg set)
def importGroup(folderNum, feats, count=200):
    arr = []
    for fileNum in xrange(1,count+1):
        arr.append(importDrive(folderNum, fileNum, feats))
    return np.concatenate(arr,axis=0)
        


def importDrive(folderNum, fileNum, feats):
    cachedFeats = cf.getCachedFeatures(folderNum, fileNum)
    #print "cachedFeats", cachedFeats
    featList = []
    todoList = []
    for feat in feats:
        hate= False
        if len(feat[2]) == 0:
            hate = True
            feat = (feat[0],feat[1],set([(None, None, 0)]))
        #print "feat", feat
        val = None
        for cachedFeat, value in cachedFeats:
            if feat == cachedFeat:
                val = value
                break
        if val is not None:
            #print "holy shit"
            featList.append((feat[0], val))
        else:
            #print "spring break"
            if hate:
                feat = (feat[0],feat[1],set([]))
            todoList.append(feat)

    if len(todoList) > 0:
        drive = getcsv.getDriver("drivers/"+str(folderNum)+"/"+str(fileNum)+".csv")
    for feat in todoList:
        func = getattr(features, feat[0])             
        argDict = {}
        for arg in feat[2]:
            argDict[arg[0]] = arg[1]
        #print func.__name__
        val = func(drive,argDict)
        featList.append((func.__name__, val))
        cf.addFeature(feat[0],feat[1],val,folderNum,fileNum,feat[2])
    featList.sort()
    featList = [val for name, val in featList]
    thing = np.array([featList])
    #print folderNum, fileNum
    #print thing
    return thing
                        
        
                
            
        
