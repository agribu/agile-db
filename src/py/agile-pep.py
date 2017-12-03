#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90db%E2%80%90policies.py
import os, re, json, argparse, sqlparse, itertools
from utils import mysqlc
from utils import policy_helper

# Main configuration file
main_conf = None
# Path to agile_conf.json
agile_conf = None
# Path to db_conf.json
db_conf = None
# Path to example_db.json
example_db = None
# Path to example_db-tables.json
example_db_tables = None
# Path to example_db-column.json
example_db_columns = None
# Path to agile-sdk-handler
agile = None

# ##################################### #
#  main function                        #
# ##################################### #
def main():
    global main_conf, agile_conf, agile, example_db, example_db_tables, example_db_columns, db_conf
    parser = argparse.ArgumentParser(description='This python script includes functions to apply example policies to existing entities')
    parser.add_argument('--conf', help='Config file',required=True)
    parser.add_argument('--checkQuery', help='Reads and applies example policies to databases', required=False)
    # parser.add_argument('--deleteDatabasePolicies', help='Reads and removes example policies to databases', action='store_true', required=False)
    # parser.add_argument('--createDatabaseTablePolicies', help='Reads and applies example policies to database tables', action='store_true', required=False)
    # parser.add_argument('--deleteDatabaseTablePolicies', help='Reads and removes example policies to database tables', action='store_true', required=False)
    # parser.add_argument('--createDatabaseColumnPolicies', help='Reads and applies example policies to database columns', action='store_true', required=False)
    # parser.add_argument('--deleteDatabaseColumnPolicies', help='Reads and removes example policies to database columns', action='store_true', required=False)
    # parser.add_argument('--createExamplePolicies', help='Reads and applies all example policies', action='store_true', required=False)
    # parser.add_argument('--removeExamplePolicies', help='Reads and removes all example policies', action='store_true', required=False)
    args = parser.parse_args()

    if args.conf:
        with open(args.conf) as json_data_file:
            main_conf = json.load(json_data_file)

        agile_conf = main_conf["agile_conf"]
        db_conf = main_conf["db_conf"]
        agile = main_conf["agile-sdk-handler"]
        example_db = main_conf["example_db"]
        example_db_tables = main_conf["example_db-tables"]
        example_db_columns = main_conf["example_db-columns"]

    if args.checkQuery:
        checkQuery(args.checkQuery)
    # if args.deleteDatabasePolicies:
    #     deleteDatabasePolicies()
    # if args.createDatabaseTablePolicies:
    #     createDatabaseTablePolicies()
    # if args.deleteDatabaseTablePolicies:
    #     deleteDatabaseTablePolicies()
    # if args.createDatabaseColumnPolicies:
    #     createDatabaseColumnPolicies()
    # if args.deleteDatabaseColumnPolicies:
    #     deleteDatabaseColumnPolicies()
    #
    # if args.createExamplePolicies:
    #     createExamplePolicies()
    # if args.removeExamplePolicies:
    #     removeExamplePolicies()

# ##################################### #
#  agile functions                      #
# ##################################### #

def getDatabase(database):
    entitytype = '{' + '"attributeType":' + '"type"' + ',' + '"attributeValue":'+ '"/db"' + '}'
    database = '{' + '"attributeType":' + '"name"' + ',' + '"attributeValue":'+ '"' + database + '"' + '}'
    constraints = '\'[' + entitytype + ', ' + database + ']\''

    debug = run(agile
        + " --conf " + agile_conf
        + " --getEntityByMultiAttributeValue"
        + " --constraints " + constraints)
    # print(debug)
    return debug

def getDatabaseTable(database, table):
    entitytype = '{' + '"attributeType":' + '"type"' + ',' + '"attributeValue":'+ '"/db-table"' + '}'
    table = '{' + '"attributeType":' + '"table"' + ',' + '"attributeValue":'+ '"' + table + '"' + '}'
    database = '{' + '"attributeType":' + '"database"' + ',' + '"attributeValue":'+ '"' + database + '"' + '}'
    constraints = '\'[' + entitytype + ', ' + database + ', ' + table + ']\''

    debug = run(agile
        + " --conf " + agile_conf
        + " --getEntityByMultiAttributeValue"
        + " --constraints " + constraints)
    # print(debug)
    return debug

def getDatabaseColumn(database, table, column):
    entitytype = '{' + '"attributeType":' + '"type"' + ',' + '"attributeValue":'+ '"/db-column"' + '}'
    table = '{' + '"attributeType":' + '"table"' + ',' + '"attributeValue":'+ '"' + table + '"' + '}'
    database = '{' + '"attributeType":' + '"database"' + ',' + '"attributeValue":'+ '"' + database + '"' + '}'
    column = '{' + '"attributeType":' + '"column"' + ',' + '"attributeValue":'+ '"' + column + '"' + '}'
    constraints = '\'[' + entitytype + ', ' + database + ', ' + table + ', ' + column + ']\''

    debug = run(agile
        + " --conf " + agile_conf
        + " --getEntityByMultiAttributeValue"
        + " --constraints " + constraints)
    # print(debug)
    return debug

def evaluatePolicy(id, type, attr, method):
    debug = run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --entityid " + id
        + " --type " + type
        + " --attr " + attr
        + " --method " + method);
    # print(debug)
    return json.loads(re.search(r"\[\s(\w+)\s\]", debug).group(1))

def setCurrentUser(token):
    debug = run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --entityid " + id
        + " --type " + type
        + " --attr " + attr
        + " --method " + method);
    # print(debug)
    # return debug

# ##################################### #
#  helper functions                     #
# ##################################### #

def run(cmd):
    nodejs = "/usr/bin/nodejs "
    return os.popen(nodejs + cmd).read()

def extractIDs(s):
    identifiers = []
    result = re.findall(r'id:+\s.+', s)
    for eid in result:
        identifiers.append(eid.split('id: ')[1].split(',')[0])
    return identifiers

def evaluateDatabasePolicy(method):
    db = mysqlc.getDatabaseName()
    db_id = extractIDs(getDatabase(db))[0]
    return evaluatePolicy(db_id, 'db', 'name', method)

def canReadDatabase():
    return evaluateDatabasePolicy('read')

def canWriteDatabase():
    return evaluateDatabasePolicy('write')

def evaluateDatabaseTablePolicy(database, table, method):
    table_id = extractIDs(getDatabaseTable(database, table))[0]
    return evaluatePolicy(table_id, 'db-table', 'table', method)

def readableTables(database):
    tables = []
    for t in mysqlc.getTables():
        if evaluateDatabaseTablePolicy(database, t, 'read'):
            tables.append(t)

    return tables

def writableTables(database):
    tables = []
    for t in mysqlc.getTables():
        if evaluateDatabaseTablePolicy(database, t, 'write'):
            tables.append(t)

    return tables

def evaluateDatabaseColumnPolicy(database, table, column, method):
    column_id = extractIDs(getDatabaseColumn(database, table, column))[0]
    return evaluatePolicy(column_id, 'db-column', 'column', method)

def readableColumns(database, table):
    columns = []
    for c in mysqlc.getColumns(table):
        if evaluateDatabaseColumnPolicy(database, table, c, 'read'):
            columns.append(c)

    return columns

def writableColumns(database, table):
    columns = []
    for c in mysqlc.getColumns(table):
        if evaluateDatabaseColumnPolicy(database, table, c, 'write'):
            columns.append(c)

    return columns

# ##################################### #
#  SQL query syntax functions           #
# ##################################### #

def isKnownTable(token):
    tables = mysqlc.getTables()
    return token.upper() in [x.upper() for x in tables]

def getTableFromQuery(query):
    for token in query.split():
        if isKnownTable(token):
            return token

    return None

def isKnownColumn(token, table):
    columns = mysqlc.getColumns(table)
    return token.upper() in [x.upper() for x in columns]

def getColumnFromQuery(query, table):
    for token in query.split():
        if isKnownColumn(token, table):
            return token

    return None

def isQueryType(token):
    types = ["SELECT", "INSERT", "ALTER", "UPDATE", "CREATE", "DROP"]
    return token.upper() in types

def getQueryType(query):
    for token in query.split():
        if isQueryType(token):
            return token

    return None

def getMethod(query_type):
    read = ["SELECT"]
    write = ["INSERT", "ALTER", "UPDATE"]
    manage = ["CREATE", "DROP"]

    if query_type.upper() in read:
        return 'read'
    elif query_type.upper() in write:
        return 'write'
    elif query_type.upper() in manage:
        return 'manage'
    else:
        return None

def hasWildcard(query):
    for token in query.split():
        if token == '*':
            return True

    return False


# ##################################### #
#  Database policy functions            #
# ##################################### #

def checkQuery(query):
    # if user can read or write anything to database, let him do it
    # else
    parseQuery(query)

def parseQuery(query):
    mysqlc.readJSONFile(db_conf)
    mysqlc.connect()
    database = mysqlc.getDatabaseName();

    query_type = getQueryType(query)
    table = getTableFromQuery(query)
    column = getColumnFromQuery(query, table)
    wildcard = hasWildcard(query)
    method = getMethod(query_type)


    print(query_type)
    print(table)
    print(column)
    print(wildcard)
    print(method)




    # print("canReadDatabase: " + str(canReadDatabase()))
    # print("canWriteDatabase: " + str(canWriteDatabase()))
    # print("readbleColumns(medical_information): ")
    # print(readableColumns(mysqlc.getDatabaseName(), 'medical_information'))
    # print("writableColumns(medical_information): ")
    # print(writableColumns(mysqlc.getDatabaseName(), 'medical_information'))

    mysqlc.terminate()

# ##################################### #
#  quick functions                      #
# ##################################### #
def createExamplePolicies():
    createDatabasePolicies()
    createDatabaseTablePolicies()
    createDatabaseColumnPolicies()

def removeExamplePolicies():
    deleteDatabasePolicies()
    deleteDatabaseTablePolicies()
    deleteDatabaseColumnPolicies()

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
