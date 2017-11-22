#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/AGILE-Database-entities
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
    parser = argparse.ArgumentParser(description='This python script includes functions to create AGILE user and group entities')
    parser.add_argument('-c','--config', help='Config file',required=True)
    parser.add_argument('--createDatabasePolicies', help='Creates some example users for testing the emergency policy scenario', action='store_true', required=False)
    parser.add_argument('--deleteDatabasePolicies', help='Deletes all example users', action='store_true', required=False)
    parser.add_argument('--createDatabaseTablePolicies', help='Creates some example groups for testing the emergency policy scenario', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseTablePolicies', help='Deletes all example groups', action='store_true', required=False)
    parser.add_argument('--createDatabaseColumnsPolicies', help='Maps example users to example groups', action='store_true', required=False)
    parser.add_argument('--deleteDatabaseColumnsPolicies', help='Deletes all mapping of example users to example groups', action='store_true', required=False)
    parser.add_argument('--createExamples', help='Creates all example users, example groups and mapping between them', action='store_true', required=False)
    parser.add_argument('--deleteExamples', help='Deletes all example users, example groups and mapping between them', action='store_true', required=False)
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
    # if args.deleteDatabasePolicies():
    #     deleteDatabasePolicies()
    # if args.createDatabaseTablePolicies:
    #     createDatabaseTablePolicies()
    # if args.deleteDatabaseTablePolicies:
    #     deleteDatabaseTablePolicies()
    # if args.createDatabaseColumnsPolicies:
    #     createDatabaseColumnsPolicies()
    # if args.deleteDatabaseColumnsPolicies:
    #     deleteDatabaseColumnsPolicies()
    # if args.createExamples:
    #     createExamples()
    # if args.deleteExamples:
    #     deleteExamples()

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

# ##################################### #
#  AGILE group functions                #
# ##################################### #
def createDatabasePolicies():
    global example_db
    rules = None
    with open(example_db) as json_data_file:
        rules = json.load(json_data_file)


    print(rules["policies"])
    policy = "'[" + ", ".join(str(x) for x in rules["policies"]) + "]'"
    entityid = extractIDs(getDatabase(rules["database"]))
    print(entityid)

    debug = run(agile
        + " --conf " + agile_conf
        + " --papSetPolicy"
        + " --entityid " + entityid[0]
        + " --type " + 'db'
        + " --attr " + 'user'
        + " --policy "
        + " --file " + '../../examples/policies/db_user_policy.json');
    print(debug)
    # return debug
# node agile-sdk-handler.js \
#     --conf agile_conf.json \
#     --papSetPolicy \
#     --entityid entityid \
#     --type 'db' \
#     --attr 'user'\
#     --policy

    # print(policies["policies"][0]["op"])
    # print(policies["policies"][0]["locks"])

# def deleteDatabasePolicies():
    # print(extractIDs(getDatabase('cdb_medical')))
# def createDatabaseTablePolicies():
    # print(extractIDs(getDatabaseTable('cdb_medical', 'patient_data')))
# def deleteDatabaseTablePolicies():
    # print(extractIDs(getDatabaseTable('cdb_medical', 'patient_data')))
# def createDatabaseColumnsPolicies():
    # print(extractIDs(getDatabaseColumn('cdb_medical', 'medical_information', 'organ_donor')))
# def deleteDatabaseColumnsPolicies():
    # print(extractIDs(getDatabaseColumn('cdb_medical', 'medical_information', 'organ_donor')))

# ##################################### #
#  quick functions                      #
# ##################################### #
# def createExamples():
#     createDatabasePolicies()
#     createDatabaseTablePolicies()
#     createDatabaseColumnsPolicies()
#
# def deleteExamples():
#     deleteDatabasePolicies()
#     deleteDatabaseTablePolicies()
#     deleteDatabaseColumnsPolicies()

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
