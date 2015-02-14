import numpy as np
from scipy.stats import rankdata
#evaluates a PU classifier

#input reqs:
#each group ought to be list consisting of ones and zeroes
#a one corresponds to a labeling as the positive (outlier) class
#a zero corresponds to a labeling of the negative (majority) class

#returns a dict giving spy recall, positive probability, and estimated F1-score
def evaluateF(unlabeledGroup, spyGroup):
    recall = float(sum(spyGroup))/len(spyGroup)

    posCount = sum(unlabeledGroup) + sum(spyGroup)
    totCount = len(unlabeledGroup) + len(spyGroup)

    posProb = float(posCount)/totCount

    score = (recall**2) / posProb
    
    result = {}
    result["recall"] = recall
    result["posProb"] = posProb
    result["score"] = score
    return  result

# estimates area under receiver operator characteristic curve
# input is scores for spy and unlabeled group
# assumes spy has only positive class
def evaluateAUC(unlabeledGroup, spyGroup):
    return ranksum(spyGroup,unlabeledGroup)

def ranksum(x,y):
    x,y = map(np.asarray, (x, y))
    n1 = len(x)
    n2 = len(y)
    alldata = np.concatenate((x,y))
    ranked = rankdata(alldata)
    x = ranked[:n1]
    y = ranked[n1:]
    s = np.sum(x,axis=0)
    maxVal = sum([x for x in xrange(n2+1, n1+n2+1)])
    return s/maxVal
