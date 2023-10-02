--create a new database
CREATE DATABASE `Company`;
USE `companyDatabase`;

--create a new schema for employee management inside the database
CREATE SCHEMA 'employeeManagement';
USE SCHEMA 'employeeManagement';

--create the employee table
CREATE TABLE employees(
  fname VARCHAR(30) NOT NULL,
  minit CHAR(20),
  lname VARCHAR(30) NOT NULL,
  ssn INT PRIMARY KEY,
  bdate DATE,
  address VARCHAR(60),
  sex VARCHAR(5),
  salary INT,
  superSsn INT,
  dno INT NOT NULL DEFAULT 1,
  FOREIGN KEY(superSsn) REFERENCES employee(ssn) ON DELETE SET NULL,
  FOREIGN KEY(dno) REFERENCES department(dnumber) ON DELETE SET DEFAULT,
  FOREIGN KEY(ssn) REFERENCES profile(ssn)
  );

--   create table department
  CREATE TABLE department (
  dnumber INT NOT NULL,
  dname VARCHAR(40) NOT NULL,
  mgrSsn INT ,
  Mgr_start_date DATE,
  PRIMARY KEY(dnumber),
  UNIQUE(dname)
);

CREATE TABLE Project(
Pname VARCHAR(30) NOT NULL,
Pnumber INT PRIMARY KEY ,
Plocation VARCHAR(30),
Dnum INT NOT NULL,
FOREIGN KEY(Dnum) REFERENCES Department(Dnumber) ON UPDATE CASCADE
);

#works on is many to many relation so it is better we maintain a relation for the relionship referencing two separate tables.
CREATE TABLE Works_On(
Essn INT NOT NULL,
Pno INT NOT NULL,
Hours TIME,
PRIMARY KEY(Essn,Pno),
FOREIGN KEY(Essn) REFERENCES Employee(Ssn) ON UPDATE CASCADE,
FOREIGN KEY(Pno) REFERENCES Project(Pnumber) ON UPDATE CASCADE
);

#Dept_location is multivalued attribute we need to main a separate relation to remove redundancy.
CREATE TABLE Dept_Locations
(
 Dnumber INT NOT NULL,
 Dlocation VARCHAR(15) NOT NULL ,
 PRIMARY KEY(Dnumber,Dlocation),
 FOREIGN KEY(Dnumber) REFERENCES Department(Dnumber) ON UPDATE CASCADE
);

#Dependent is a weak entity.It refered along with a refrencing relation called Ess which is made part of the table as Essn.
#A employee cant have dependent with all the fields identical
CREATE TABLE Dependent
(
 Essn INT,
 Dependent_name VARCHAR(15),
 Sex CHAR,
 Bdate DATE,
 Relationship VARCHAR(20),
 PRIMARY KEY(Essn,Dependent_name),
 FOREIGN KEY(Essn) REFERENCES Employee(Ssn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE Dependent
DROP COLUMN Sex,
ADD COLUMN Sex CHAR(1);




