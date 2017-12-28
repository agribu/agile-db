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
echo "## CREATE AND DELETE EXAMPLE DATABASE POLICIES"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabasePolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabasePolicies

echo
echo "## CREATE AND DELETE EXAMPLE DATABASE TABLE POLICIES"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabaseTablePolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabaseTablePolicies

echo
echo "## CREATE AND DELETE EXAMPLE DATABASE COLUMN POLICIES"
echo
./agile-db-policies.py --conf conf/local_conf.json --createDatabaseColumnPolicies
./agile-db-policies.py --conf conf/local_conf.json --deleteDatabaseColumnPolicies

echo
echo "## CREATE AND DELETE ALL EXAMPLE POLICIES"
echo
./agile-db-policies.py --conf conf/local_conf.json --createExamplePolicies
./agile-db-policies.py --conf conf/local_conf.json --removeExamplePolicies

echo
echo "## Success for agile-db-policies.py!"
echo
