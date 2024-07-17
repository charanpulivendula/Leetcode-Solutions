# Write your MySQL query statement below
select p.project_id, round(Avg(e.experience_years),2) as average_years
from project as p inner join employee as e
on p.employee_id = e.employee_id
group by p.project_id
