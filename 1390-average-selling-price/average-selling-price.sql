# Write your MySQL query statement below
select p.product_id, coalesce(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price 
from prices as p left join UnitsSold as u 
on u.product_id = p.product_id 
and u.purchase_date >= p.start_date 
and u.purchase_date<=p.end_date
group by p.product_id
-- having u.product_id is nopt null

