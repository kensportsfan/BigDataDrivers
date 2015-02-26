from scipy.spatial.distance import euclidean
import numpy as np

#gets duration of the drive in seconds
def getDuration(drive):
    return float(len(drive))

#gets the distance of the drive in meters
def getDistance(drive):
    dist = 0
    for i in xrange(len(drive)-1):
        dist += euclidean(drive[i],drive[i+1])
    return dist
    #return float(reduce(lambda x, y : (x[0] + euclidean(x[0],y), y), drive, (0,[0,0]))[0])

#OPTIMIZE ME
def getAvgSpeed(drive):
    dur = getDuration(drive)
    return 0 if dur <= 0 else getDistance(drive)/dur

def getAllFeatures(drive):
    return {"duration":getDuration(drive),"distance":getDistance(drive), 
            "avgSpeed":getAvgSpeed(drive)}

def computeFeatures(drive,feats):
    allFeats = getAllFeatures(drive)
    data = []
    for feature in feats:
        data.append(allFeats[feature])
    return np.array(data)
