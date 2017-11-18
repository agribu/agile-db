#!/usr/bin/python3
import mysqlc, os

agile = "../js/agile-sdk-handler/agile-sdk-handler"
db_ctr = 0
tab_ctr = 0
col_ctr = 0

def run(cmd):
    nodejs = "/usr/bin/nodejs "
    return os.popen(nodejs + cmd).read()

def createDatabase():
    global db_ctr
    db_ctr += 1
    debug = run(agile
        + " --createEntity"
        + " --id " + str(db_ctr)
        + " --type " + "'db'"
        + " --name " + mysqlc.config["name"])
    print(debug) # debug output

    for key, value in mysqlc.config.items():
        if key not in "name":
            debug = run(agile
                + " --setEntityAttribute"
                + " --id " + str(db_ctr)
                + " --type " + "'db'"
                + " --attr " + key
                + " --value " + value)
        print(debug) # debug output

def createTables():
    global tab_ctr
    tables = mysqlc.getTables()
    for table in tables:
        tab_ctr += 1
        debug = run(agile
            + " --createDatabaseColumn"
            + " --id " + str(tab_ctr)
            + " --type " + "'db-table'"
            + " --database " + mysqlc.config["name"]
            + " --table " + table)
        print(debug)

def createColumns(table):
    global col_ctr
    columns = mysqlc.getColumns(table)
    debug = table + " : " + ','.join(columns)
    for column in columns:
        col_ctr += 1
        debug = run(agile
            + " --createDatabaseColumn"
            + " --id " + str(col_ctr)
            + " --type " + "'db-column'"
            + " --database " + mysqlc.config["name"]
            + " --table " + table
            + " --column " + column)
        print(debug)

def createAllColumns():
    for t in mysqlc.getTables():
        createColumns(t)

# mysqlc.readJSONFile("../../conf/db_conf.json")
# mysqlc.connect()
# print(mysqlc.getTables()[0])
# print(mysqlc.getDatabaseName())
# print(mysqlc.getColumns("patient_data"))
# print(mysqlc.executeQuery("select * from patient_data;"))
# print(mysqlc.getJSONStructure())


# print(run(agile + " --deleteEntity --id " + str(0) + " --type 'database'"))
# print(run(agile + " --getEntityByType --type 'db-column'"))

# createDatabase()
# createTables()
# createAllColumns()

# mysqlc.terminate()
