#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90db%E2%80%90policies.py
import os, re, json, argparse, sqlparse, itertools
from utils import mysqlc
from utils import helpers

# Main configuration file
main_conf = None
# Path to agile_conf.json
agile_conf = None
# Path to db_conf.json
db_conf = None
# Path to agile-sdk-handler
agile = None

# ##################################### #
#  main function                        #
# ##################################### #
def main():
    global main_conf, agile_conf, agile, db_conf
    parser = argparse.ArgumentParser(description='This python script includes functions to apply example policies to existing entities')
    parser.add_argument('--conf', help='Config file',required=True)
    parser.add_argument('--checkQuery', help='Reads and applies example policies to databases', action='store_true', required=False)
    parser.add_argument('--query', help='Reads and applies example policies to databases', required=False)
    parser.add_argument('--token', help='Reads and applies example policies to databases', required=False)
    parser.add_argument('--db', help='Reads and applies example policies to databases', required=False)
    args = parser.parse_args()

    if args.conf:
        with open(args.conf) as json_data_file:
            main_conf = json.load(json_data_file)

        helpers.initialize(args.conf)

        agile_conf = main_conf["agile_conf"]
        db_conf = main_conf["db_conf"]
        agile = main_conf["agile-sdk-handler"]

    if args.checkQuery:
        checkQuery(args.query, args.token, args.db)

# ##################################### #
#  Database policy functions            #
# ##################################### #

def getCurrentToken():
    debug = helpers.run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --idmTokenGet ");
    # print(debug)
    return debug.strip()

def setCurrentToken(token):
    debug = helpers.run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --idmTokenSet " + token);
    # print(debug)
    return debug.strip()

def checkQuery(query, token, db_id):
    # db_id = 'cdb_medical@localhost:3307'

    # helpers.switchUser(token)
    parseQuery(query, db_id)
    # helpers.resetUserToken()

def parseQuery(query, db_id):
    try:
        db_entity = helpers.getExistingDatabase(db_id)

        if db_entity != ['[]']:
            # Build database config from existing entity
            db_entity = helpers.getJSON(db_entity)[0]
            db_entity.pop('id', None)
            db_entity.pop('type', None)
            db_entity.pop('owner', None)
            mysqlc.setConfig(db_entity)

            mysqlc.connect()
            database = db_entity["name"];
            evaluateQuery(db_id, query, database)
            mysqlc.terminate()
        else:
            raise Exception("SQL operation failed!")
    except Exception as e:
        print(e)
        mysqlc.terminate()


def evaluateQuery(db_id, query, database):
    queryType = helpers.getMethod(helpers.getQueryType(query))

    print("Evaluating Query! Please stand by ...")
    if queryType == 'read':
        database_cond = helpers.canReadDatabase
        table_cond = helpers.canReadTable
        column_cond = helpers.canReadColumn
    elif queryType == 'write':
        database_cond = helpers.canWriteDatabase
        table_cond = helpers.canWriteTable
        column_cond = helpers.canWriteColumn
    else:
        raise Exception("Something is wrong with the SQL query type!")

    if database_cond():
        result = mysqlc.executeQuery(query)[0]
    else:
        table = helpers.getTableFromQuery(query)
        table_cond = table_cond(database, table)
        if table_cond | (helpers.hasWildcard(query) & table_cond):
            print("table")
            result = mysqlc.executeQuery(query)[0]
        else:
            column = helpers.getColumnFromQuery(query, table)
            if column_cond(database, table, column):
                print("col")
                result = mysqlc.executeQuery(query)[0]
            else:
                raise Exception("SQL operation: Permission denied!")

    # Check for query result and print flattened output
    print(list(itertools.chain(result)) if result != None else "")

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
