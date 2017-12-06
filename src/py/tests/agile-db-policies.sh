#!/bin/bash
echo "## Create and delete example database policies"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabasePolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabasePolicies
echo
echo "## Create and delete example database table policies"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabaseTablePolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabaseTablePolicies
echo
echo "## Create and delete example database column policies"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabaseColumnPolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabaseColumnPolicies
echo
echo "## Create and delete all example policies"
echo
./agile-db-policies.py --conf conf/local_conf.json --createExamplePolicies
./agile-db-policies.py --conf conf/local_conf.json --removeExamplePolicies
echo
echo "## Success for agile-db-policies.py"
echo
