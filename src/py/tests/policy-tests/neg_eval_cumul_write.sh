echo "###################################################"
echo "## EVALUATE NEGATIVE POLICY TESTS"

echo
echo "### WRITE OPERATIONS FOR OWNER"

echo
echo "#### OWNER SHOULDN'T BE ABLE TO WRITE EXCESSIVE_ALCOHOL TO HISTORY_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'update history_data set excessive_alcohol = 0 where excessive_alcohol = 1;'\
                --db 'cdb_medical@localhost:3307'\
                --token $owner_token

echo
echo "#### PARAMEDIC SHOULDN'T BE ABLE TO WRITE ID TO PATIENT_DATA"
echo
./agile-pep.py --conf conf/local_conf.json\
                --query 'update patient_data set id = 1 where id = 0;'\
                --db 'cdb_medical@localhost:3307'\
                --token $paramed_token
