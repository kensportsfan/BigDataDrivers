import sqlite3
import sqlInit

#Only call once
#Better protections to be implemented later
def populateDrives(folderCount=25, fileCount=200):
    connection = sqlInit.getConnection()
    items = []
    for i in xrange(1,folderCount+1):
        for j in xrange(1, fileCount+1):
            items.append((i, j))
    stmt = "INSERT INTO drives (folder, file) VALUES (?,?)"
    c = connection.cursor()
    c.executemany(stmt, items)
    connection.commit()
