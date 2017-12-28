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
echo "###################################################"
echo "## EVALUATE NEGATIVE POLICY TESTS"

echo
echo "### READ OPERATIONS FOR PARAMEDIC"
echo
echo "#### PARAMEDIC SHOULDN'T BE ABLE TO READ ANYTHING FROM PATIENT_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from patient_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token
