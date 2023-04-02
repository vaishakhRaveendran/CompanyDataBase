USE `Company`;


#Retrieve bdate and address of employee whose name is 'john b smith'
select Bdate,Address
from employee 
where Fname='john' AND Minit='B' and Lname='Smith';


#Retrieve the name and adress of all employee who works for the research department
#select-project-join 
select Fname,Lname,Address
from Employee,Department
where Dname= 'Research' and Dnumber=Dno;

#Self referencing relation
#Using the as key to remove the ambuigity.
select E.Lname,S.Lname
from Employee as E,Employee as S
where E.Super_ssn =S.Ssn;


#Rename the relation attributes within the query in sql by giving alias in the from clause
-- select  *
-- from Department as E(A,B,L,C,D);



#Make a list of all the project numbers for projects that involves employee whose last name is "Smith' either as a worker or as a manager of the department
#that controls the project.

(
	select distinct Pnumber Id
	from works_on W,Employee E
	where W.Essn=E.Ssn and E.Lname='Smith'
)
union
(
   select distinct Pnumber Id
   from Employee,Department,Projects
   where Lname='Smith' and Ssn=Mgr_ssn and Dnumber=Dnum
);
