import pueval
import numpy as np
import labeleval

def testPUClassifier(classifier, unlabeledData, spyData, normalizer):
    unlabeledRes, spyRes= classifier(unlabeledData, spyData)
    unlabeledRes = normalizer(unlabeledRes)
    spyRes = normalizer(spyRes)
    return pueval.evaluate(unlabeledRes, spyRes)

def testSupervisedClassifier(classifier,unlabeledData, labels, normalizer,
                             showGraph=False,
                             title='Receiver operating characteristic curve'):

    predictions, _ = classifier(unlabeledData, unlabeledData[0:0])
    predictions = normalizer(predictions)
    return labeleval.rocArea(labels, predictions, showGraph=showGraph,
                             title=title)
