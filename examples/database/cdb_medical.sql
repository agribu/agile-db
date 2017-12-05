-- This template is based on https://github.com/openemr/openemr/blob/e0def8f04986fa8c75d7bc485304db4a7d9dd699/Documentation/Database.pdf

-- drop database cdb_medical;
create database cdb_medical;
use cdb_medical;

CREATE TABLE patient_data (
    id int,
    fname varchar(255), -- First name
    lname varchar(255), -- Last name
    sex varchar(255),
    DOB varchar(255) , -- Date of Birth
    address varchar(255),
    added varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE emergency_contact (
    id int, -- ID of entry
    fname varchar(255), -- First name
    lname varchar(255), -- Last name
    sex varchar(255),
    DOB varchar(255) , -- Date of Birth
    address varchar(255),
    contact_relationship varchar(255),
    added varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE medical_information (
    id int, -- ID of entry
    bloodtype varchar(255),
    high_blood_pressure int,
    heart_problems int,
    pregnancy int,
    organ_donor int,
    added varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE history_data (
    id int, -- ID of entry
    excessive_alcohol int,
    heart_surgery int,
    added varchar(255), -- Date of entry
    pid int -- ID of patient
);

INSERT INTO patient_data (id, fname, lname, sex, DOB, address, added, pid)
VALUES (0, "Hans", "Peter", "male", "11/23/1976", "Amselweg. 16, 45896 Gelsenkirchen", "11/05/2017", 0);

INSERT INTO emergency_contact (id, fname, lname, sex, DOB, address, contact_relationship, added, pid)
VALUES (0, "Nicole", "Peter", "female", "08/13/1923", "Mauerstr. 13, 45896 Gelsenkirchen", "Mother", "11/05/2017", 0);

INSERT INTO medical_information (id, bloodtype, high_blood_pressure, heart_problems, pregnancy, organ_donor, added, pid)
VALUES (0, "AB", 1, 0, 1, 0, "11/05/2017", 0);

INSERT INTO history_data (id, excessive_alcohol, heart_surgery, added, pid)
VALUES (0, 1, 1, "11/05/2017", 0);
