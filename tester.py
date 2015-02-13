import pueval
import numpy as np
import labeleval

def testPUClassifier(classifier, unlabeledData, spyData, normalizer):
    unlabeledRes, spyRes= classifier(unlabeledData, spyData)
    comb = np.append(unlabeledRes, spyRes)
    comb = normalizer(comb)
    n = len(unlabeledRes)
    return pueval.evaluateAUC(comb[:n], comb[n:])

def testSupervisedClassifier(classifier,unlabeledData, labels, normalizer,
                             showGraph=False,
                             title='Receiver operating characteristic curve'):

    predictions, _ = classifier(unlabeledData, unlabeledData[0:0])
    predictions = normalizer(predictions)
    return labeleval.rocArea(labels, predictions, showGraph=showGraph,
                             title=title)
