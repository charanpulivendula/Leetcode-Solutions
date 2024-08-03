# Write your MySQL query statement below
WITH ManagerStayed as (
    SELECT e1.employee_id
    FROM Employees e1 join Employees e2
    ON e2.manager_id = e1.employee_id
)


SELECT employee_id
From Employees
WHERE manager_id 
NOT IN (
    SELECT * from ManagerStayed
)
AND manager_id IS NOT NULL
AND salary < 30000
ORDER BY employee_id ASC
