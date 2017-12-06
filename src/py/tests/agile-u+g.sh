#!/bin/bash
echo "## CREATE AND DELETE EXAMPLE USER ENTITIES"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleUsers
./agile-u+g.py --conf conf/local_conf.json --deleteExampleUsers

echo
echo "## CREATE AND DELETE EXAMPLE GROUPS"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleGroups
./agile-u+g.py --conf conf/local_conf.json --deleteExampleGroups

echo
echo "## CREATE AND DELETE EXAMPLE MAPPINGS USER-GROUP"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleUsers
./agile-u+g.py --conf conf/local_conf.json --createExampleGroups
./agile-u+g.py --conf conf/local_conf.json --createMappings
./agile-u+g.py --conf conf/local_conf.json --deleteMappings
./agile-u+g.py --conf conf/local_conf.json --deleteExampleGroups
./agile-u+g.py --conf conf/local_conf.json --deleteExampleUsers

echo
echo "## CREATE AND DELETE ALL ENTITIES"
echo
./agile-u+g.py --conf conf/local_conf.json --createExamples
./agile-u+g.py --conf conf/local_conf.json --deleteExamples

echo
echo "## Success for agile-u+g.py!"
echo
