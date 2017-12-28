#!/usr/bin/python3
# /*******************************************************************************
#  * Copyright (c) Benjamin Schuermann.
#  * All rights reserved. This program and the accompanying materials
#  * are made available under the terms of the Eclipse Public License v1.0
#  * which accompanies this distribution, and is available at
#  * http://www.eclipse.org/legal/epl-v10.html
#  *
#  * Contributors:
#  *     Benjamin Schuermann
#  ******************************************************************************/
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
    parser.add_argument('--query', help='Reads and applies example policies to databases', required=True)
    parser.add_argument('--token', help='Reads and applies example policies to databases', required=True)
    parser.add_argument('--db', help='Reads and applies example policies to databases', required=True)
    args = parser.parse_args()

    if args.conf:
        with open(args.conf) as json_data_file:
            main_conf = json.load(json_data_file)

        helpers.initialize(args.conf)

        agile_conf = main_conf["agile_conf"]
        db_conf = main_conf["db_conf"]
        agile = main_conf["agile-sdk-handler"]

        initialize(args.query, args.token, args.db)

# ##################################### #
#  Database policy functions            #
# ##################################### #
def initialize(query, token, db_id):
    # db_id = 'cdb_medical@localhost:3307'

    try:
        db_entity = helpers.getExistingDatabase(db_id)

        if db_entity != ['[]']:
            db_entity = helpers.getJSON(db_entity)[0]
            db_id = db_entity["id"]

            # Build database config from existing entity
            db_entity.pop('id', None)
            db_entity.pop('type', None)
            db_entity.pop('owner', None)
            mysqlc.setConfig(db_entity)

            mysqlc.connect()
            database = db_entity["name"]

            # helpers.switchUser(token)
            # helpers.switchUser(token)
            evaluateQuery(db_id, query, database, token)
            # helpers.resetUserToken()

            mysqlc.terminate()
        else:
            raise Exception("SQL operation failed!")
    except Exception as e:
        print(e)
        mysqlc.terminate()


def evaluateQuery(db_id, query, database, token):
    helpers.usertoken = token
    queryType = helpers.getMethod(helpers.getQueryType(query))
    result = None

    print("Evaluating Query! Please stand by ...")

    # Determine query type
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

    # policy evaluation
    if database_cond(db_id):
        # print("db_cond")
        result = mysqlc.executeQuery(query)
        result = result[0] if result != None else None
    else:
        # print("before tab_cond")
        table = helpers.getTableFromQuery(query)
        table_cond = table_cond(database, table)
        if table_cond:
            # print("tab_cond")
            result = mysqlc.executeQuery(query)
            result = result[0] if result != None else None
        else:
            # print("else tab_cond")
            if helpers.hasWildcard(query):
                # print("wild")
                raise Exception("Policy Evaluation for SQL query: Permission denied!")
            else:
                # print("else wild")
                column = helpers.getColumnFromQuery(query, table)
                if column_cond(database, table, column):
                    # print("col_cond")
                    result = mysqlc.executeQuery(query)
                    result = result[0] if result != None else None
                else:
                    # print("final else")
                    raise Exception("Policy Evaluation for SQL query: Permission denied!")

    # Check for query result and print flattened output
    print(list(itertools.chain(result)) if result != None else "")

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
