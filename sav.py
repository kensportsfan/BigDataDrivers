from os import path

def readSav(filename):
    if path.isfile(filename):
        with open(filename, 'r') as f:
            return eval(f.read())
    else:
        return {}

def writeSav(filename, featdict):
    with open(filename, 'w') as f:
        f.write(str(featdict))
        
