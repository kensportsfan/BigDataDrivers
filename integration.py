import featureimport as fi
import demo
import normalize

def test():
    feats = ["duration","distance","avgSpeed"]
    unlabeled = fi.importGroup("drivers/1",feats)
    outliers = fi.importGroup("drivers/2",feats)
    data = (unlabeled, outliers[:10], 0)
    fullScore = demo.demoPU(data=data, n_features=unlabeled.shape[1],
                norm=normalize.doNothing)
    print("one done")
    feats = ["duration"]
    unlabeled = fi.importGroup("drivers/1",feats)
    outliers = fi.importGroup("drivers/2",feats)
    data = (unlabeled, outliers[:10], 0)
    durScore = demo.demoPU(data=data, n_features=unlabeled.shape[1],
                norm=normalize.doNothing)
    print "Full Score: ", fullScore
    print "Duration Score: ", durScore

test()
