# Write your MySQL query statement below
-- select employee_id,name 
-- from employees
-- where employee_id =
    (
        select e2.reports_to as employee_id,e1.name,count(e2.reports_to) as reports_count,
        round(avg(e2.age)) as average_age 
        from employees e1 left join employees e2 
        on e1.employee_id = e2.reports_to
        group by (e2.reports_to)
        having e2.reports_to is not null
        order by e1.employee_id
    )
