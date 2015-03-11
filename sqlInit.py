import sqlite3

connection = None

def getConnection():
    global connection
    if connection is None:
        connection = sqlite3.connect('featureCache.db')
    return connection

def closeConnection():
    global connection
    if connection is not None:
        connection.close()
        connection = None

def createTables():
    conn = getConnection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS drives
                (id INTEGER PRIMARY KEY,
                folder INTEGER NOT NULL,
                file INTEGER NOT NULL)''')
    c.execute('''CREATE INDEX IF NOT EXISTS labels ON drives (folder, file)''')

    c.execute('''CREATE TABLE IF NOT EXISTS features
                (id INTEGER PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                version INTEGER NOT NULL,
                value FLOAT NOT NULL,
                driverId INTEGER NOT NULL,
                FOREIGN KEY(driverId) REFERENCES drives(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS args
                (id INTEGER PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                featureId INTEGER NOT NULL,
                stringValue VARCHAR(255),
                intValue INTEGER,
                floatValue DOUBLE,
                FOREIGN KEY(featureId) REFERENCES features(id))''')
    conn.commit()

def refreshTable(name):
    stmt = "DROP TABLE ?"
    conn = getConnection()
    c = conn.cursor()
    c.execute(stmt, (name,))
    createTables()

    closeConnection()

createTables()
