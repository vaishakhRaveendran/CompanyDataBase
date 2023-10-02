-- --create a new schema for employee management inside the database
CREATE SCHEMA `employeeManagement`;
USE  `employeeManagement`;

-- -----------------------------DEPARTMENT INFO------------------------------------
--  create table department
 CREATE TABLE departments (
  dnumber INT NOT NULL,
  dname VARCHAR(40) NOT NULL,
  mgrSsn INT DEFAULT 133557799, 
  mgrStartDate DATE,
  PRIMARY KEY (dnumber),
  UNIQUE (dname)
);

-- --create deptlocations relation
CREATE TABLE deptLocations
(
 dnumber INT NOT NULL,
 dlocation VARCHAR(15) NOT NULL ,
 PRIMARY KEY(dnumber,dlocation),
 FOREIGN KEY(dnumber) REFERENCES departments(dnumber) ON UPDATE CASCADE ON DELETE CASCADE
);

-- --------------------------EMPLOYEE INFO---------------------------------------------------
-- create the stack pool
CREATE TABLE stacks(
 stack VARCHAR(20),
 id INT PRIMARY KEY);

-- --create the employee table
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
  FOREIGN KEY(dno) REFERENCES departments(dnumber) ON DELETE SET DEFAULT,
  FOREIGN KEY(superSsn) REFERENCES employees(ssn) ON DELETE SET NULL
);
ALTER TABLE departments ADD FOREIGN KEY (mgrSsn) REFERENCES employees(ssn) ON DELETE SET DEFAULT;

 -- create skill set of employee
 CREATE TABLE skills(
  employeeSsn INT,
  stackId INT,
  PRIMARY KEY(employeeSSn,stackId) ,
  FOREIGN KEY(stackId) REFERENCES stacks(id),
  FOREIGN KEY(employeeSSn) REFERENCES employees(ssn) ON DELETE CASCADE
  );


-- -------------PROJECT INFO---------------------------------------------------------------
-- --create project
CREATE TABLE projects(
pname VARCHAR(30) NOT NULL,
pnumber INT PRIMARY KEY ,
plocation VARCHAR(30),
dnum INT NOT NULL,
FOREIGN KEY(dnum) REFERENCES departments(dnumber) ON UPDATE CASCADE
);
-- --create project requirement
CREATE TABLE projectRequirements(
pnumber INT PRIMARY KEY,
stackId INT,
FOREIGN KEY(pnumber) REFERENCES projects(pnumber) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (stackId) REFERENCES stacks(id) ON UPDATE CASCADE
);
-- --create worksOn relation
CREATE TABLE worksOn(
employeeSsn INT NOT NULL,
pno INT NOT NULL,
hours TIME,
PRIMARY KEY(employeeSsn,pno),
FOREIGN KEY(employeeSsn) REFERENCES employees(ssn) ON UPDATE CASCADE,
FOREIGN KEY(pno) REFERENCES projects(pnumber) ON UPDATE CASCADE ON DELETE CASCADE
);





