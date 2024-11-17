--test db queries:
CREATE TABLE TEST (
ID INT,
NAME VARCHAR(30), --anna csak 4 karakternyi helyet foglal
--NAME_CHAR CHAR(30) --anna 30 karakternyi helyet foglal
ADDRESS VARCHAR(50)
)


INSERT INTO TEST (ID, NAME, ADDRESS) VALUES (2, 'PAnna', 'y street 6')

select * from test

update test set name = 'Laci' where id = 1

delete from test where name = 'Laci'

--beszélj foreign és primary key-ekről!!

-- List All Employees with Their Departments
SELECT e.employee_id, e.full_name, d.department_name
FROM employee e
left JOIN department d ON e.department_id = d.department_id;

--Find All Employees Managed by John Smith (Assuming employee_id = 1)

SELECT e.employee_id, e.full_name, e.job_role
FROM employee e
WHERE e.manager_id = (select employee_id from employee e2 where full_name = 'John Smith'); --1 eredetileg


--Display Each Department with the Number of Employees
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM department d
LEFT JOIN employee e ON d.department_id = e.department_id
GROUP BY d.department_name;

--Find Departments Without Employees

SELECT d.department_name
FROM department d
LEFT JOIN employee e ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;


--Retrieve Hierarchical Employee Reporting Structure
SELECT e1.full_name AS Employee, e2.full_name AS Manager
FROM employee e1
LEFT JOIN employee e2 ON e1.manager_id = e2.employee_id
ORDER BY e2.full_name, e1.full_name;

--Departments with More Than Two Employees

-- using CTE (common table expression)
with department_employee_count as (
select department_name,  count(e.employee_id) as employee_count
from department d
left join employee e on d.department_id = e.department_id 
group by d.department_name
order by department_name desc
)

select * from department_employee_count
where employee_count > 2

--using HAVING

SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM department d
JOIN employee e ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 2;









-- ADDITIONAL IF REQUIRED



--List All Job Roles and the Number of Employees in Each Role

SELECT e.job_role, COUNT(*) AS num_employees
FROM employee e
GROUP BY e.job_role
ORDER BY num_employees DESC;