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
