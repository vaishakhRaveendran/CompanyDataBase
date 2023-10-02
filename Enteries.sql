USE employeeManagement;
INSERT INTO projects(pname, pnumber, plocation, dnum) VALUES
('ProductX', 1, 'Bellaire', 3),
('ProductY', 2, 'Sugarland', 2),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 5),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 6);

INSERT INTO worksOn(employeeSsn,pno,hours) VALUES
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
(3, 'Stafford'),
(5, 'Bellaire'),
(2, 'Sugarland'),
(6, 'Houston');
