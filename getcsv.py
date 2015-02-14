from numpy import genfromtxt

#simple wrappers for getting driver data from csv

# gets a single drive from a single file, contained in a numpy array
# contains x, y coordinates in meters, taken every second
def getDriver(filename):
    return genfromtxt(filename, delimiter=',',skip_header=1)

# gets all 200 drives from a folder
# returns an ordered list of drives 
def getGroup(foldername, count=200):
    return [getDriver(foldername+"/"+str(i)+".csv") for i in xrange(1, 201)]
