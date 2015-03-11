import sqlite3
import sqlInit

#Only call once
#Better protections to be implemented later
def populateDrives(folderCount=4000, fileCount=200):
    connection = sqlInit.getConnection()
    items = []
    for i in xrange(1,folderCount+1):
        for j in xrange(1, fileCount+1):
            items.append((i, j))
    stmt = "INSERT INTO drives (folder, file) VALUES (?,?)"
    c = connection.cursor()
    c.executemany(stmt, items)
    connection.commit()

#arg format:
    #(name, value, type)
    #types: 0 = string, 1 = int, 2 = float
def addFeature(name, version, value, folderNum, fileNum, args):
    folderNum = folderNum[8:]
    connection = sqlInit.getConnection()
    stmt = '''INSERT INTO features (name, version, value, driverId)
                VALUES (?,?,?,
                (SELECT id FROM drives
                    WHERE folder=?
                    AND file=?))'''
    c = connection.cursor()
    c.execute(stmt, (name, version, value, folderNum, fileNum))
    featureId = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    stmt = '''INSERT INTO args (name, featureId, stringValue, intValue, floatValue)
                VALUES (?, ?, ?, ?, ?)'''
    for name, value, dType in args:
        #print "sjhdf"
        vals = [name, featureId, None, None, None]
        vals[dType+2] = value
        c.execute(stmt, vals)
        
    connection.commit()

def getCachedFeatures(folderNum, fileNum):
    folderNum = folderNum[8:]
    connection = sqlInit.getConnection()
    c = connection.cursor()
    stmt = '''SELECT f.id, f.name, f.version, f.value, a.name, stringValue, intValue, floatValue
                FROM drives JOIN features AS f ON
                drives.id = f.driverId AND
                folder = ? AND
                file = ?
                LEFT JOIN args AS a ON
                f.id = a.featureId'''
    c.execute(stmt, (folderNum, fileNum))
    args = c.fetchall()
    features = {}
    for fId, fName, fVersion, fValue, aName, strVal, intVal, floatVal in args:
        if (fId, fName, fVersion, fValue) not in features.keys():
            features[(fId, fName, fVersion, fValue)] = set([])
        val = None
        dType = 0
        val=None
        if strVal:
            val = strVal
        elif intVal:
            val = intVal
            dType = 1
        elif floatVal:
            val = floatVal
            dType = 2
        features[(fId, fName, fVersion, fValue)].add((aName,val,dType))
    featList = []
    for feat, args in features.iteritems():
        item = ((feat[1],feat[2],args),feat[3])
        featList.append(item)
    return featList
    
