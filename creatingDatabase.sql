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
  FOREIGN KEY(superSsn) REFERENCES employees(ssn) ON DELETE SET NULL
);

INSERT INTO employees(fname, minit, lname, ssn, bdate, address,sex, salary,superSsn,dno) VALUES
('Roosevelt', 'D', 'Franklin', 123456009, '1923-01-09', '731-Fondren-Spring-TX', 'M', 80000, NULL,5),
('Jennifer', 'S', 'Wallace', 987654321, '1941-06-20', '291-Berry-Bellaire-TX', 'F', 43000, NULL, 6),
('James', 'E', 'Borg', 888665555, '1937-11-10', '450-Stone-Houston-TX', 'M', 55000, NULL, 1),
('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321-Castle-Spring-TX', 'F', 25000, 987654321, 6),
('Ahmad', 'V', 'Jabbar', 987987987, '1969-03-29', '980-Dallas-Houston-TX', 'M', 25000, 987654321, 3),
('Monica', 'E', 'Hailey', 987614321, '1981-06-20', '291-Berry-Terrace-TX', 'F', 43000, 888665555, 4),
('Franklin', 'T', 'Wong', 333445555, '1955-12-08', '638-Voss-Houston-TX', 'M', 40000, 888665555, 7),
('John', 'B', 'Smith', 123456789, '1965-01-09', '731-Fondren-Houston-TX', 'M', 30000, 333445555,5),
('Ramesh', 'K', 'Narayan', 666884444, '1962-09-15', '975-Fire-Oak-Humble-TX', 'M', 38000, 333445555, 1),
('Joyce', 'A', 'English', 453453453, '1972-07-31', '5631-Rice-Houston-TX', 'F', 25000, 333445555, 7);

INSERT INTO departments VALUES
(5,'Research', 333445555, '1988-05-22'),
(2,'IT_Support', 987654321, '1998-05-22'),
(4,'Administration', 666884444,'1995-01-01'),
(7,'Production', 888665555, '1985-06-19'),
(8,'Development', 123456789, '1981-03-19'),
(6,'Testing', 987987987, '1981-08-15'),
(1,'Trainee', 453453453, '1989-06-19'),
(3,'Headquarters',123456009, '1981-06-19');
ALTER TABLE departments ADD FOREIGN KEY (mgrSsn) REFERENCES employees(ssn) ON DELETE SET DEFAULT;
ALTER TABLE employees ADD  FOREIGN KEY(dno) REFERENCES departments(dnumber) ON DELETE SET DEFAULT;

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





