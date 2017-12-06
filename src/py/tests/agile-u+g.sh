#!/bin/bash
echo "## Create and delete example user entities"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleUsers
./agile-u+g.py --conf conf/local_conf.json --deleteExampleUsers
echo
echo "## Create and delete example groups"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleGroups
./agile-u+g.py --conf conf/local_conf.json --deleteExampleGroups
echo
echo "## Create and delete example mappings user-group"
echo
./agile-u+g.py --conf conf/local_conf.json --createExampleUsers
./agile-u+g.py --conf conf/local_conf.json --createExampleGroups
./agile-u+g.py --conf conf/local_conf.json --createMappings
./agile-u+g.py --conf conf/local_conf.json --deleteMappings
./agile-u+g.py --conf conf/local_conf.json --deleteExampleGroups
./agile-u+g.py --conf conf/local_conf.json --deleteExampleUsers
echo
echo "## Create and delete all entities"
echo
./agile-u+g.py --conf conf/local_conf.json --createExamples
./agile-u+g.py --conf conf/local_conf.json --deleteExamples
echo
echo "## Success for agile-u+g.py"
echo
