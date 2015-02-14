import csv
import demo
import normalize

# runs through demos to create a csv containing a data lake of test runs
# created to evaluate ranksum test as a predictor of AUC
# ranges should be tuples indicating start and finish values for range to test
# repeats is how many samples for each treatment
def genData(unlabeledRange=(200,201),outlierRange=(2,7),featureRange=(2,3),
            pollutionRange=(0,50),norm=normalize.doNothing, repeats=1,multiplierRange=(1,5),
            filename='regression.csv'):
    myfile = open(filename,'wb')
    wr = csv.writer(myfile)
    wr.writerow(["predictedAUC","actualAUC","unlabeledCount","spyCount","pollutionCount",
                     "featureCount","multiplier"])
    i = 0
    fullData = []
    for unlabeled in xrange(unlabeledRange[0],unlabeledRange[1]):
        for outlier in xrange(outlierRange[0], outlierRange[1]):
            for feat in xrange(featureRange[0],featureRange[1]):
                for pollution in xrange(pollutionRange[0],pollutionRange[1]):
                    for multiplier in xrange(multiplierRange[0],multiplierRange[1]):
                        for repeat in xrange(0,repeats):
                            i+=1
                            print "THE CURRENT SAMPLE IS: ", i
                            data = demo.demoData(n_samples=unlabeled,n_outliers=outlier,
                                                 n_features=feat, pollution=pollution,
                                                 outlierMultiplier=multiplier)
                            res = demo.demoAUCcomp(data=data, norm=norm)
                            wr.writerow([res["pu"],res["sup"],unlabeled,outlier,pollution,
                                             feat,multiplier])

    myfile.close()
                    
