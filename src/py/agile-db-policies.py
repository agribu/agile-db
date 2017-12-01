#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90db%E2%80%90policies.py
import os, re, json, argparse
from utils import mysqlc

# Main configuration file
main_conf = None
# Path to agile_conf.json
agile_conf = None
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
    global main_conf, agile_conf, agile, example_db, example_db_tables, example_db_columns
    parser = argparse.ArgumentParser(description='This python script includes functions to apply example policies to existing entities')
    parser.add_argument('-c','--config', help='Config file',required=True)
    parser.add_argument('--createDatabasePolicies', help='Reads and applies example policies to databases', action='store_true', required=False)
    parser.add_argument('--deleteDatabasePolicies', help='Reads and removes example policies to databases', action='store_true', required=False)
    parser.add_argument('--createDatabaseTablePolicies', help='Reads and applies example policies to database tables', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseTablePolicies', help='Reads and removes example policies to database tables', action='store_true', required=False)
    parser.add_argument('--createDatabaseColumnPolicies', help='Reads and applies example policies to database columns', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseColumnPolicies', help='Reads and removes example policies to database columns', action='store_true', required=False)
    parser.add_argument('--createExamplePolicies', help='Reads and applies all example policies', action='store_true', required=False)
    parser.add_argument('--removeExamplePolicies', help='Reads and removes all example policies', action='store_true', required=False)
    args = parser.parse_args()

    if args.config:
        with open(args.config) as json_data_file:
            main_conf = json.load(json_data_file)

        agile_conf = main_conf["agile_conf"]
        db_conf = main_conf["db_conf"]
        agile = main_conf["agile-sdk-handler"]
        example_db = main_conf["example_db"]
        example_db_tables = main_conf["example_db-tables"]
        example_db_columns = main_conf["example_db-columns"]

    if args.createDatabasePolicies:
        createDatabasePolicies()
    if args.deleteDatabasePolicies:
        deleteDatabasePolicies()
    if args.createDatabaseTablePolicies:
        createDatabaseTablePolicies()
    if args.deleteDatabaseTablePolicies:
        deleteDatabaseTablePolicies()
    if args.createDatabaseColumnPolicies:
        createDatabaseColumnPolicies()
    if args.deleteDatabaseColumnPolicies:
        deleteDatabaseColumnPolicies()

    if args.createExamplePolicies:
        createExamplePolicies()
    if args.removeExamplePolicies:
        removeExamplePolicies()

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

def setPolicy(id, type, attr, policy):
    debug = run(agile
        + " --conf " + agile_conf
        + " --papSetPolicy"
        + " --entityid " + id
        + " --type " + type
        + " --attr " + attr
        + " --policy " + policy);
    # print(debug)
    # return debug
    print("Successfully applied policies to " + id + "!")

def unsetPolicy(id, type, attr, policy):
    debug = run(agile
        + " --conf " + agile_conf
        + " --papDeletePolicy"
        + " --entityid " + id
        + " --type " + type
        + " --attr " + attr);
    # print(debug)
    # return debug
    print("Successfully removed policies from " + id + "!")

# ##################################### #
#  Example policy functions             #
# ##################################### #
def createDatabasePolicies():
    global example_db
    array = None
    with open(example_db) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabase(rules["database"]))
        setPolicy(entityid[0], 'db', 'name', policy)

def createDatabaseTablePolicies():
    global example_db_tables
    array = None

    with open(example_db_tables) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabaseTable(rules["database"], rules["table"]))
        setPolicy(entityid[0], 'db-table', 'table', policy)

def createDatabaseColumnPolicies():
    global example_db_columns
    array = None

    with open(example_db_columns) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabaseColumn(rules["database"], rules["table"], rules["column"]))
        setPolicy(entityid[0], 'db-column', 'column', policy)

def deleteDatabasePolicies():
    global example_db
    array = None
    with open(example_db) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabase(rules["database"]))
        unsetPolicy(entityid[0], 'db', 'name', policy)

def deleteDatabaseTablePolicies():
    global example_db_tables
    array = None

    with open(example_db_tables) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabaseTable(rules["database"], rules["table"]))
        unsetPolicy(entityid[0], 'db-table', 'table', policy)

def deleteDatabaseColumnPolicies():
    global example_db_columns
    array = None

    with open(example_db_columns) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = extractIDs(getDatabaseColumn(rules["database"], rules["table"], rules["column"]))
        unsetPolicy(entityid[0], 'db-column', 'column', policy)

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
