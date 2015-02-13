import featureimport as fi
import demo

def test():
    feats = ["duration","distance","avgSpeed"]
    unlabeled = fi.importGroup("drivers/1",feats)
    outliers = fi.importGroup("drivers/2",feats)
    data = (unlabeled, outliers[:10], 0)
    demo.demoPU(data=data, n_features=unlabeled.shape[1])

test()
