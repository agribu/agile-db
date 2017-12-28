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
import os, re, json, argparse, sqlparse, itertools
from utils import mysqlc
# Main configuration file
main_conf = None
# Path to agile_conf.json
agile_conf = None
# Path to db_conf.json
db_conf = None
# Path to agile-sdk-handler
agile = None
# User token for switchUser function
usertoken = None

# ##################################### #
#  main function                        #
# ##################################### #
def main():
    print("Start helpers.py")

def initialize(conf):
    global agile, agile_conf, main_conf
    with open(conf) as json_data_file:
        main_conf = json.load(json_data_file)
    agile_conf = main_conf["agile_conf"]
    agile = main_conf["agile-sdk-handler"]

# ##################################### #
#  helper functions                     #
# ##################################### #

def run(cmd):
    nodejs = "/usr/bin/nodejs "
    return os.popen(nodejs + cmd).read()

def getJSON(s):
    for x in re.findall('\w+:', s):
        s = re.sub(x, "\"" + re.split(':',x)[0] + "\":", s)
        s = s.replace("'", "\"")
    return json.loads(s)

def switchUser(token):
    global agile_conf
    with open(agile_conf) as json_data_file:
        conf = json.load(json_data_file)

    conf["token"] = token
    agile_conf = "'" + str(conf).replace("'", "\"") + "'"

    if getCurrentUserInfo() == None:
        raise Exception("Invalid user token!")
    # else:
    #     print("User switched! Current user: " + getCurrentUserInfo()["id"])

def resetUserToken():
    global agile_conf, main_conf
    agile_conf = main_conf["agile_conf"]
    # print("User restored! Current user: " + getCurrentUserInfo()["id"])

# ##################################### #
#  agile functions                      #
# ##################################### #

def getCurrentUserInfo():
    debug = run(agile
        + " --conf " + agile_conf
        + " --getCurrentUserInfo");
    # return debug
    return None if (debug == "") else getJSON(debug)

def getCurrentToken():
    debug = run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --idmTokenGet ");
    # print(debug)
    return debug.strip()

def setCurrentToken(token):
    debug = run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --idmTokenSet " + token);
    # print(debug)
    return debug.strip()

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

def getExistingDatabase(identifier):
    split = re.split('@', identifier)
    database = split[0]
    split = re.split(':', split[1])
    host = split[0]
    port = split[1]

    entitytype = '{' + '"attributeType":' + '"type"' + ',' + '"attributeValue":'+ '"/db"' + '}'
    db_constr = '{' + '"attributeType":' + '"name"' + ',' + '"attributeValue":'+ '"' + database + '"' + '}'
    host_constr = '{' + '"attributeType":' + '"host"' + ',' + '"attributeValue":'+ '"' + host + '"' + '}'
    port_constr = '{' + '"attributeType":' + '"port"' + ',' + '"attributeValue":'+ '"' + port + '"' + '}'
    constraints = '\'[' + entitytype + ', ' + db_constr + ', ' + host_constr + ', ' + port_constr + ']\''

    debug = run(agile
        + " --conf " + agile_conf
        + " --getEntityByMultiAttributeValue"
        + " --constraints " + str(constraints))
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

def evaluatePolicy(eid, etype, attr, method):
    global usertoken
    if usertoken != None: switchUser(usertoken)
    debug = run(agile
        + " --conf " + agile_conf
        + " --pdpEvaluate"
        + " --entityid " + eid
        + " --type " + etype
        + " --attr " + attr
        + " --method " + method);
    # print("PolicyEval for " + eid + "by user " + getCurrentUserInfo()["id"] + ":" + debug)
    if usertoken != None: resetUserToken()
    return getJSON(debug)[0]

# ##################################### #
#  policy functions                     #
# ##################################### #

def evaluateDatabasePolicy(method, database):
    # db = mysqlc.getDatabaseName()
    # db_id = getJSON(getDatabase(db))[0]["id"]
    return evaluatePolicy(database, 'db', 'policy_setting', method)

def canReadDatabase(database):
    return evaluateDatabasePolicy('read', database)

def canWriteDatabase(database):
    return evaluateDatabasePolicy('write', database)

def evaluateDatabaseTablePolicy(database, table, method):
    table_id = getJSON(getDatabaseTable(database, table))[0]["id"]
    return evaluatePolicy(table_id, 'db-table', 'policy_setting', method)

def readableTables(database):
    tables = []
    for t in mysqlc.getTables():
        print(t)
        if evaluateDatabaseTablePolicy(database, t, 'read'):
            tables.append(t)

    return tables

def canReadTable(database, table):
    # return table in readableTables(database)
    return evaluateDatabaseTablePolicy(database, table, 'read')

def writableTables(database):
    tables = []
    for t in mysqlc.getTables():
        if evaluateDatabaseTablePolicy(database, t, 'write'):
            tables.append(t)

    return tables

def canWriteTable(database, table):
    # return table in writableTables(database)
    return evaluateDatabaseTablePolicy(database, table, 'write')

def evaluateDatabaseColumnPolicy(database, table, column, method):
    # print(database + ", " + table + ", " + column + ", " + method)
    column_id = getJSON(getDatabaseColumn(database, table, column))[0]["id"]
    return evaluatePolicy(column_id, 'db-column', 'policy_setting', method)

def readableColumns(database, table):
    columns = []
    for c in mysqlc.getColumns(table):
        if evaluateDatabaseColumnPolicy(database, table, c, 'read'):
            columns.append(c)

    return columns

def canReadColumn(database, table, column):
    # return column in readableColumns(database, table)
    return evaluateDatabaseColumnPolicy(database, table, column, 'read')

def writableColumns(database, table):
    columns = []
    for c in mysqlc.getColumns(table):
        if evaluateDatabaseColumnPolicy(database, table, c, 'write'):
            columns.append(c)

    return columns

def canWriteColumn(database, table, column):
    # return column in writableColumns(database, table)
    return evaluateDatabaseColumnPolicy(database, table, column, 'write')

# ##################################### #
#  SQL query syntax functions           #
# ##################################### #

def isKnownTable(token):
    tables = mysqlc.getTables()
    return token.upper() in [x.upper() for x in tables]

def getTableFromQuery(query):
    for token in query.split():
        # Remove special chracters from string
        token = re.sub('[^\w\.]+', '', token)
        if isKnownTable(token):
            return token

    return None

def isKnownColumn(token, table):
    columns = mysqlc.getColumns(table)
    return token.upper() in [x.upper() for x in columns]

def getColumnFromQuery(query, table):
    for token in query.split():
        # Remove special chracters from string
        token = re.sub('[^\w\.]+', '', token)
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
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
