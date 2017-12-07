#!/bin/bash
echo "###################################################"
echo "## EVALUATE POSITIVE POLICY TESTS"

echo
echo "### READ OPERATIONS FOR OWNER"

echo
echo "#### OWNER SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from medical_information;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token

echo
echo "#### OWNER SHOULD BE ABLE TO READ ID FROM PATIENT_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select id from patient_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token

echo
echo "#### OWNER SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token

echo
echo "#### OWNER SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select excessive_alcohol from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token


echo
echo "### READ OPERATIONS FOR DOCTOR"

echo
echo "#### DOCTOR SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from medical_information;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo
echo "#### DOCTOR SHOULD BE ABLE TO READ ID FROM PATIENT_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select id from patient_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo
echo "#### DOCTOR SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo
echo "#### DOCTOR SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select excessive_alcohol from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo
echo "### READ OPERATIONS FOR PARAMEDIC"

echo
echo "#### PARAMEDIC SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token

echo
echo "#### PARAMEDIC SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select excessive_alcohol from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token
