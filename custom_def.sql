USE employeemanagement;
-- Finding all the available projects
 select distinct pnumber from projects;


--Create the function for finding stack required for the project
 SELECT s.stack, pr.pnumber
 FROM stacks s
 INNER JOIN projectrequirements pr ON s.Id = pr.stackId;
 WHERE pr.pnumber = 2;



-- Finding employee matching skills required for the project
select pr.stackId,sk.employeeSsn
from skills as sk
right join projectrequirements as pr on pr.stackId=sk.stackId
where pr.pnumber =2;


