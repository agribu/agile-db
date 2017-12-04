#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90db%E2%80%90policies.py
import os, re, json, argparse
from utils import helpers

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
    parser.add_argument('--conf', help='Config file',required=True)
    parser.add_argument('--createDatabasePolicies', help='Reads and applies example policies to databases', action='store_true', required=False)
    parser.add_argument('--deleteDatabasePolicies', help='Reads and removes example policies to databases', action='store_true', required=False)
    parser.add_argument('--createDatabaseTablePolicies', help='Reads and applies example policies to database tables', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseTablePolicies', help='Reads and removes example policies to database tables', action='store_true', required=False)
    parser.add_argument('--createDatabaseColumnPolicies', help='Reads and applies example policies to database columns', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseColumnPolicies', help='Reads and removes example policies to database columns', action='store_true', required=False)
    parser.add_argument('--createExamplePolicies', help='Reads and applies all example policies', action='store_true', required=False)
    parser.add_argument('--removeExamplePolicies', help='Reads and removes all example policies', action='store_true', required=False)
    args = parser.parse_args()

    if args.conf:
        with open(args.conf) as json_data_file:
            main_conf = json.load(json_data_file)
        helpers.initialize(args.conf)

        agile_conf = main_conf["agile_conf"]
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
#  Example policy functions             #
# ##################################### #
def createDatabasePolicies():
    global example_db
    array = None
    with open(example_db) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabase(rules["database"]))
        helpers.setPolicy(entityid[0], 'db', 'name', policy)

def createDatabaseTablePolicies():
    global example_db_tables
    array = None

    with open(example_db_tables) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabaseTable(rules["database"], rules["table"]))
        helpers.setPolicy(entityid[0], 'db-table', 'table', policy)

def createDatabaseColumnPolicies():
    global example_db_columns
    array = None

    with open(example_db_columns) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabaseColumn(rules["database"], rules["table"], rules["column"]))
        helpers.setPolicy(entityid[0], 'db-column', 'column', policy)

def deleteDatabasePolicies():
    global example_db
    array = None
    with open(example_db) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabase(rules["database"]))
        helpers.unsetPolicy(entityid[0], 'db', 'name', policy)

def deleteDatabaseTablePolicies():
    global example_db_tables
    array = None

    with open(example_db_tables) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabaseTable(rules["database"], rules["table"]))
        helpers.unsetPolicy(entityid[0], 'db-table', 'table', policy)

def deleteDatabaseColumnPolicies():
    global example_db_columns
    array = None

    with open(example_db_columns) as json_data_file:
        array = json.load(json_data_file)

    for rules in array:
        policy = "'[" + ", ".join(str(x) for x in rules["policies"]).replace("'", "\"") + "]'"
        entityid = helpers.extractIDs(helpers.getDatabaseColumn(rules["database"], rules["table"], rules["column"]))
        helpers.unsetPolicy(entityid[0], 'db-column', 'column', policy)

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
