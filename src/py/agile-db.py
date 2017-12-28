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
# Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90db.py
import os, re, json, argparse
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

# Helper: counter for database id creation
db_ctr = 0
# Helper: counter for table id creation
tab_ctr = 0
# Helper: counter for column id creation
col_ctr = 0

# ##################################### #
#  main function                        #
# ##################################### #
def main():
    global main_conf, agile_conf, db_conf, agile
    parser = argparse.ArgumentParser(description='This python script includes functions to translate a database with its tables and columns into AGILE entities')
    parser.add_argument('--conf', help='Config file',required=True)
    parser.add_argument('--createDatabase', help='Creates a database entity based on a provided configuration', action='store_true', required=False)
    parser.add_argument('--createTables', help='Creates table entities from the configured database', action='store_true', required=False)
    parser.add_argument('--createColumns', help='Creates column entities from the configured database', action='store_true', required=False)
    parser.add_argument('--deleteAll', help='Deletes all entities of a particular type', required=False)
    parser.add_argument('--dbInit', help='Creates the database, and all tables and column entites', action='store_true', required=False)
    parser.add_argument('--dbReset', help='Deletes the database, and all tables and column entites', action='store_true', required=False)
    args = parser.parse_args()

    if args.conf:
        with open(args.conf) as json_data_file:
            main_conf = json.load(json_data_file)

        helpers.initialize(args.conf)

        agile_conf = main_conf["agile_conf"]
        db_conf = main_conf["db_conf"]
        agile = main_conf["agile-sdk-handler"]

        mysqlc.readJSONFile(db_conf)
        mysqlc.connect()

        if args.createDatabase:
            createDatabase()
        if args.createTables:
            createTables()
        if args.createColumns:
            createAllColumns()
        if args.deleteAll:
            typename = args.deleteAll
            deleteAll(typename)
        if args.dbInit:
            dbInit()
        if args.dbReset:
            dbReset()

        mysqlc.terminate()

# ##################################### #
#  database functions                   #
# ##################################### #
def setPolicyAttribute(eid, etype, polattr):
    debug = helpers.run(agile
        + " --conf " + agile_conf
        + " --setEntityAttribute"
        + " --id " + eid
        + " --type " + etype
        + " --attr " + "policy_setting"
        + " --value " + polattr)
    print(debug) # debug output

def createDatabase():
    global db_ctr
    db_ctr += 1
    db_id = mysqlc.config["name"] + "!@!db"
    print(db_id)
    debug = helpers.run(agile
        + " --conf " + agile_conf
        + " --createDatabase"
        + " --id " + db_id
        + " --type " + "'db'"
        + " --name " + mysqlc.config["name"])
    print(debug) # debug output

    for key, value in mysqlc.config.items():
        if key not in "name":
            debug = helpers.run(agile
                + " --conf " + agile_conf
                + " --setEntityAttribute"
                + " --id " + db_id
                + " --type " + "'db'"
                + " --attr " + key
                + " --value " + value)
        print(debug) # debug output

def createTables():
    global tab_ctr
    tables = mysqlc.getTables()
    for table in tables:
        tab_ctr += 1
        db_tab_id = str(tab_ctr) + "-" + mysqlc.config["name"] + "!@!db-table"
        debug = helpers.run(agile
            + " --conf " + agile_conf
            + " --createDatabaseColumn"
            + " --id " + db_tab_id
            + " --type " + "'db-table'"
            + " --database " + mysqlc.config["name"]
            + " --table " + table)
        print(debug)
        setPolicyAttribute(db_tab_id, "'db-table'", mysqlc.config["policy_setting"])

def createColumn(table, index, c):
    # TODO both lines needed somewhere?
    columns = mysqlc.getColumns(table)
    debug = table + " : " + ','.join(columns)

    col_id = index + "-" + mysqlc.config["name"] + "!@!db-column"

    debug = helpers.run(agile
        + " --conf " + agile_conf
        + " --createDatabaseColumn"
        + " --id " + col_id
        + " --type " + "'db-column'"
        + " --database " + mysqlc.config["name"]
        + " --table " + table
        + " --column " + c)
    print(debug)
    setPolicyAttribute(col_id, "'db-column'", mysqlc.config["policy_setting"])

def createAllColumns():
    global tab_ctr, col_ctr
    tab_ctr = 0
    col_ctr = 0
    for t in mysqlc.getTables():
        tab_ctr += 1
        for c in mysqlc.getColumns(t):
            col_ctr += 1
            createColumn(t, str(tab_ctr) + "." + str(col_ctr), c)
        col_ctr = 0

def deleteAll(typename):
    result = helpers.run(agile
        + " --conf " + agile_conf
        + " --getEntityByType"
        + " --type " + typename)
    if result != "":
        for x in helpers.getJSON(result):
            debug = helpers.run(agile
                + " --conf " + agile_conf
                + " --deleteEntity"
                + " --id " + x["id"]
                + " --type " + typename)
            print(debug + " - " + x["id"])
    else:
        print("No entities to delete for type " + typename)

# ##################################### #
#  quick functions                      #
# ##################################### #
def dbInit():
    createDatabase()
    createTables()
    createAllColumns()

def dbReset():
    deleteAll("db")
    deleteAll("db-table")
    deleteAll("db-column")

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
