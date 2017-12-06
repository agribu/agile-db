#!/bin/bash
echo "## CREATE AND DELETE DATABASE ENTITY"
echo
./agile-db.py --conf conf/local_conf.json --createDatabase
./agile-db.py --conf conf/local_conf.json --delete 'db'

echo
echo "## CREATE AND DELETE DATABASE TABLE ENTITIES"
echo
./agile-db.py --conf conf/local_conf.json --createTables
./agile-db.py --conf conf/local_conf.json --delete 'db-table'

echo
echo "## CREATE AND DELETE DATABASE COLUMN ENTITIES"
echo
./agile-db.py --conf conf/local_conf.json --createColumns
./agile-db.py --conf conf/local_conf.json --delete 'db-column'

echo
echo "## CREATE AND DELETE ALL ENTITIES"
echo
./agile-db.py --conf conf/local_conf.json --dbInit
./agile-db.py --conf conf/local_conf.json --dbReset

echo
echo "## Success for agile-db.py!"
echo
