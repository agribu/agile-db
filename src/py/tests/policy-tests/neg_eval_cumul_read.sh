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
