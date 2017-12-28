#!/bin/bash
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
