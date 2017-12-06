#!/bin/bash
echo "###################################################"
echo "## EVALUATE POSITIVE POLICY CONDITIONS FOR DATABASE"
echo
echo "#### OWNER SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from medical_information;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token

echo
echo "#### DOCTOR SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from medical_information;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo
echo "#### DOCTOR SHOULD BE ABLE TO WRITE ANYTHING TO MEDICAL_INFORMATION (-> ID)"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'update medical_information set id = 1 where id = 0;'\
                --db 'cdb_medical@localhost:3307'\
                --token $doctor_token

echo "###################################################"
echo "## EVALUATE NEGATIVE POLICY CONDITIONS FOR DATABASE"
echo
echo "#### PARAMEDIC SHOULDN'T BE ABLE TO READ ANYTHING FROM PATIENT_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from patient_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token

echo
echo "#### PARAMEDIC SHOULDN'T BE ABLE TO READ ANYTHING FROM HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'select * from history_data;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token

echo
echo "#### PARAMEDIC SHOULDN'T BE ABLE TO WRITE ANYTHING TO PATIENT_DATA (-> ID)"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'update patient_data set id = 1 where id = 0;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token

echo
echo "## Success for database policy evaluation!"
echo
