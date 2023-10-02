USE  `employeeManagement`;
INSERT INTO departments VALUES
(5,'Research', 333445555, '1988-05-22'),
(4,'Administration', 987654321,'1995-01-01'),
(7,'Production', 888665505, '1985-06-19'),
(8,'Development', 888665555, '1981-03-19'),
(1,'Trainee', 888665155, '1989-06-19'),
(3,'Headquarters', 838665555, '1981-06-19');

INSERT INTO employees(fname, minit, lname, ssn, bdate, address,sex, salary,superSsn,dno) VALUES
('John', 'B', 'Smith', 123456789, '1965-01-09', '731-Fondren-Houston-TX', 'M', 30000, 333445555,5),
('Franklin', 'T', 'Wong', 333445555, '1955-12-08', '638-Voss-Houston-TX', 'M', 40000, 888665555, 5),
('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321-Castle-Spring-TX', 'F', 25000, 987654321, 4),
('Jennifer', 'S', 'Wallace', 987654321, '1941-06-20', '291-Berry-Bellaire-TX', 'F', 43000, 888665555, 4),
('Ramesh', 'K', 'Narayan', 666884444, '1962-09-15', '975-Fire-Oak-Humble-TX', 'M', 38000, 333445555, 5),
('Joyce', 'A', 'English', 453453453, '1972-07-31', '5631-Rice-Houston-TX', 'F', 25000, 333445555, 5),
('Ahmad', 'V', 'Jabbar', 987987987, '1969-03-29', '980-Dallas-Houston-TX', 'M', 25000, 987654321, 4),
('James', 'E', 'Borg', 888665555, '1937-11-10', '450-Stone-Houston-TX', 'M', 55000, NULL, 1);

INSERT INTO project(pname, pnumber, plocation, dnum) VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4);

INSERT INTO works_on(employeeSsn,pno,hours) VALUES
(123456789, 1, 32.5),
(123456789, 2, 7.5),
(666884444, 3, 40.0),
(453453453, 1, 20.0),
(453453453, 2, 20.0),
(333445555, 2, 10.0),
(333445555, 3, 10.0),
(333445555, 10, 10.0),
(333445555, 20, 10.0),
(999887777, 30, 30.0),
(999887777, 10, 10.0),
(987987987, 10, 35.00),
(987987987, 30, 5.0),
(987654321, 30, 20.0),
(987654321, 20, 15.0),
(888665555, 20, NULL);

INSERT INTO deptLocations(dnumber, dlocation)VALUES
(1, 'Houston'),
(4, 'Stafford'),
(5, 'Bellaire'),
(5, 'Sugarland'),
(5, 'Houston');
