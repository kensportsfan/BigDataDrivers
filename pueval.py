#evaluates a PU classifier

#input reqs:
#each group ought to be list consisting of ones and zeroes
#a one corresponds to a labeling as the positive (outlier) class
#a zero corresponds to a labeling of the negative (majority) class
def evaluate(unlabeledGroup, spyGroup):
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

#it is possible that this may also work with probabilities in the data
#I think that in this case, our metric will mimic the area under the ROC curve
#more research req
