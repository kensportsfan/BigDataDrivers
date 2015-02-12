import normalize
from sklearn import metrics
import matplotlib.pyplot as plt


def evaluate(actual, predicted):
    fp = tp = fn = tn = 0
    for i in xrange(len(predicted)):
        if predicted[i] > 0:
            if actual[i] >0:
                tp += 1
            else:
                fp += 1
        else:
            if actual[i] <= 0:
                tn += 1
            else:
                fn += 1
    return {"fp":fp,"tp":tp,"fn":fn,"tn":tn}

def rocArea(actual, predicted, showGraph=False,
             title='Receiver operating characteristic curve'):
    
    fpr, tpr, _ = metrics.roc_curve(actual, predicted)
    auc = metrics.auc(fpr, tpr)
    if showGraph:
        displayROC(fpr, tpr, auc, title)
    return auc

def displayROC(fpr, tpr, auc, title):
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()
