# STARTING POLICY EVALUATION TESTS

###################################################
## EVALUATE POSITIVE POLICY TESTS

### READ OPERATIONS FOR OWNER

#### OWNER SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION

Evaluating Query! Please stand by ...
['0', 'AB', '1', '0', '1', '0', '11/05/2017', '0']

#### OWNER SHOULD BE ABLE TO READ ID FROM PATIENT_DATA

Evaluating Query! Please stand by ...
['0']

#### OWNER SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['0', '1', '1', '11/05/2017', '0']

#### OWNER SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['1']

### READ OPERATIONS FOR DOCTOR

#### DOCTOR SHOULD BE ABLE TO READ ANYTHING FROM MEDICAL_INFORMATION

Evaluating Query! Please stand by ...
['0', 'AB', '1', '0', '1', '0', '11/05/2017', '0']

#### DOCTOR SHOULD BE ABLE TO READ ID FROM PATIENT_DATA

Evaluating Query! Please stand by ...
['0']

#### DOCTOR SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['0', '1', '1', '11/05/2017', '0']

#### DOCTOR SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['1']

### READ OPERATIONS FOR PARAMEDIC

#### PARAMEDIC SHOULD BE ABLE TO READ ANYTHING FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['0', '1', '1', '11/05/2017', '0']

#### PARAMEDIC SHOULD BE ABLE TO READ EXCESSIVE_ALCOHOL FROM HISTORY_DATA

Evaluating Query! Please stand by ...
['1']
###################################################
## EVALUATE NEGATIVE POLICY TESTS

### READ OPERATIONS FOR PARAMEDIC

#### PARAMEDIC SHOULDN'T BE ABLE TO READ ANYTHING FROM PATIENT_DATA

Evaluating Query! Please stand by ...
Policy Evaluation for SQL query: Permission denied!
###################################################
## EVALUATE NEGATIVE POLICY TESTS

### WRITE OPERATIONS FOR OWNER

#### OWNER SHOULDN'T BE ABLE TO WRITE EXCESSIVE_ALCOHOL TO HISTORY_DATA

Evaluating Query! Please stand by ...
Policy Evaluation for SQL query: Permission denied!

#### PARAMEDIC SHOULDN'T BE ABLE TO WRITE ID TO PATIENT_DATA

Evaluating Query! Please stand by ...
Policy Evaluation for SQL query: Permission denied!

# Success for agile-pep.py!

