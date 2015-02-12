from numpy import genfromtxt

def getDriver(filename):
    return genfromtxt(filename, delimiter=',',skip_header=1)

def getGroup(foldername, count=200):
    return [getDriver(foldername+"/"+str(i)+".csv") for i in xrange(1, 201)]
