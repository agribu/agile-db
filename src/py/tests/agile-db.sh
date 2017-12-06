#!/bin/bash
echo "## Create and delete database entity"
echo
./agile-db.py --conf conf/local_conf.json --createDatabase
./agile-db.py --conf conf/local_conf.json --delete 'db'
echo
echo "## Create and delete database table entities"
echo
./agile-db.py --conf conf/local_conf.json --createTables
./agile-db.py --conf conf/local_conf.json --delete 'db-table'
echo
echo "## Create and delete database column entities"
echo
./agile-db.py --conf conf/local_conf.json --createColumns
./agile-db.py --conf conf/local_conf.json --delete 'db-column'
echo
echo "## Create and delete all entities"
echo
./agile-db.py --conf conf/local_conf.json --dbInit
./agile-db.py --conf conf/local_conf.json --dbReset
echo
echo "## Success for agile-db.py"
echo
