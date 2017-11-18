#!/usr/bin/python3
# Documentation available: https://github.com/agribu/agile-db/wiki/SQL-Operations
import pymysql, json, re, argparse

# Database connection
conn = None
# Connection cursor
cur = None
# Configuration file
config = None

# ##################################### #
#  main function                        #
# ##################################### #
def main():
    global inputfile
    parser = argparse.ArgumentParser(description='This script executes operations on a configured database.')
    parser.add_argument('-i','--input', help='Config file',required=True)
    parser.add_argument('--getDatabase', help='Database name', action='store_true', required=False)
    parser.add_argument('--getTables', help='Database tables as list', action='store_true', required=False)
    parser.add_argument('--getJSONStructure', help='Retrieve Database as JSON Structure', action='store_true', required=False)
    parser.add_argument('--getColumns', help='Database table columns as list', required=False)
    parser.add_argument('--executeQuery', help='Execute SQL query', required=False)
    args = parser.parse_args()

    if args.input:
        inputfile = args.input
        readJSONFile(inputfile)
        connect()

        if args.getDatabase:
            print(getDatabaseName())
        if args.getJSONStructure:
            print(getJSONStructure())
        if args.executeQuery:
            query = args.executeQuery
            print(executeQuery(query))
        if args.getTables:
            print(getTables())
        if args.getColumns:
            table = args.getColumns
            print(getColumns(table))

        terminate()

# ##################################### #
#  helper functions                     #
# ##################################### #
def readJSONFile(inputfile):
    global config
    # Read configuration file
    with open(inputfile) as json_data_file:
        config = json.load(json_data_file)

def setConfig(conf):
    global config
    config = conf

# ##################################### #
#  connection functions                 #
# ##################################### #
def connect():
    global conn, cur, config
    conn = pymysql.connect(
            host=str(config["host"]),
            port=int(config["port"]),
            user=str(config["user"]),
            passwd=str(config["password"]),
            db=str(config["name"]))

    cur = conn.cursor()

def terminate():
    global conn, cur
    cur.close()
    conn.close()

# ##################################### #
#  database functions                   #
# ##################################### #
def getDatabaseName():
    global config
    return str(config["database"])

def getTables():
    global conn, cur
    cur.execute("show tables;")
    raw = cur.fetchall()
    return re.findall('\w+', str(raw))

def getColumns(table):
    global conn, cur
    cur.execute("select * from " + table + ";")
    raw = re.findall(r"'\w+'", str(cur.description))
    sub = re.sub(r"(u')|'","", str(raw))
    cols = re.findall(r'"\w+"', sub)
    columns = []
    for c in cols:
        columns.append(re.sub("\"", "", c))
    return columns

def executeQuery(query):
    global conn, cur
    cur.execute(query)
    return cur.fetchall()

# ##################################### #
#  export functions                     #
# ##################################### #
def getJSONStructure():
    global conn, cur, config
    database = []
    basic = []
    tables = []

    basic.append({"db_host":config["host"]})
    basic.append({"db_port":config["port"]})
    basic.append({"db_user":config["user"]})
    basic.append({"db_name":config["database"]})

    for t in getTables():
        name = t
        table = []
        table.append({"name":name})

        columns = []
        for c in getColumns(name):
            columns.append({"name":c})

        table.append({"columns":columns})
        tables.append(table)

    basic.append({"tables":tables})
    database.append({"database":basic})
    json_data = json.dumps(database, indent=2, sort_keys=True)

    return json_data

# ##################################### #
#  start                                #
# ##################################### #
if __name__ == "__main__":
   main()
