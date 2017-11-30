-- This template is based on https://github.com/openemr/openemr/blob/e0def8f04986fa8c75d7bc485304db4a7d9dd699/Documentation/Database.pdf

-- drop database cdb_medical; 
create database cdb_medical; 
use cdb_medical;

CREATE TABLE patient_data (
    id int,
    title varchar(255),
    fname varchar(255), -- First name
    lname varchar(255), -- Last name
    mname varchar(255), -- Middle name
    sex varchar(255),
    DOB varchar(255) , -- Date of Birth
    street varchar(255),
    postal_code varchar(255),
    city varchar(255),
    state varchar(255),
    country_code varchar(255),
    ss varchar(255), -- Social Security Number
    occupation varchar(255),
    phone_home varchar(255),
    phone_biz varchar(255),
    phone_mobile varchar(255),
    date varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE emergency_contact (
    id int, -- ID of entry
    title varchar(255), -- Mr., Mrs., etc.
    fname varchar(255), -- First name
    lname varchar(255), -- Last name
    mname varchar(255), -- Middle name
    sex varchar(255),
    DOB varchar(255) , -- Date of Birth
    street varchar(255),
    postal_code varchar(255),
    city varchar(255),
    state varchar(255),
    country_code varchar(255),
    phone_home varchar(255),
    phone_biz varchar(255),
    phone_mobile varchar(255),
    contact_relationship varchar(255),
    date varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE medical_information (
    id int, -- ID of entry    
    bloodtype varchar(255),
    high_blood_pressure int,
    epilepsy int,
    heart_problems int,
    diabetes int,
    haemophilia int, -- blood sickness
    pregnancy int,
    organ_donor int,
    allergies int,
    date varchar(255), -- Date of entry
    pid int -- ID of patient
);

CREATE TABLE history_data (
    id int, -- ID of entry
    excessive_coffee int,
    excessive_tobacco int,
    excessive_alcohol int,
    exercise_level int,
    heart_surgery int,
    hysterectomy int,
    hernia_repair int,
    hip_replacement int,
    knee_replacement int,
    date varchar(255), -- Date of entry
    pid int -- ID of patient
);

INSERT INTO patient_data (id, title, fname, lname, sex, DOB, street, postal_code, city, state, country_code, ss, occupation, phone_home, date, pid) VALUES (0, "Mr.", "Hans", "Peter", "male", "11/23/1976", "Mauerstr. 13", "45896", "Gelsenkirchen", "North-Rhine-Westphalia", "DE", "041-60-0954", "Electrician", "04512353642", "11/05/2017", 0);

INSERT INTO emergency_contact (id, title, fname, lname, sex, DOB, street, postal_code, city, state, country_code, phone_home, contact_relationship, date, pid) VALUES (0, "Mrs.", "Nicole", "Peter", "male", "08/13/1923", "Mauerstr. 13", "45896", "Gelsenkirchen", "North-Rhine-Westphalia", "DE", "04512353642", "Mother", "11/05/2017", 0);

INSERT INTO medical_information (id, bloodtype, high_blood_pressure, epilepsy, heart_problems, diabetes, haemophilia, pregnancy, organ_donor, allergies, date, pid) VALUES (0, "AB", 1, 0, 1, 0, 0, 0, 1, 1, "11/05/2017", 0);

INSERT INTO history_data (id, excessive_coffee, excessive_tobacco, excessive_alcohol, exercise_level, heart_surgery, hysterectomy, hernia_repair, hip_replacement, knee_replacement, date, pid) VALUES (0, 0, 0, 1, 2, 1, 0, 0, 0, 1, "11/05/2017", 0);
