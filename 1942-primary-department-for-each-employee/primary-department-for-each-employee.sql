select e1.employee_id,e1.department_id 
from employee e1 
where e1.primary_flag = "Y" or
e1.employee_id in (
    select employee_id 
    from employee
    group by employee_id
    having count(employee_id) = 1
)
-- group by (e2.employee_id)
-- having count(e2.employee_id) = 1 or e1.primary_flag = "Y"
