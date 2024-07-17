# Write your MySQL query statement below
select q1.query_name, round(Avg(q1.rating/position),2) as quality,
(
    select round(count(q2.rating)*100/count(q1.rating),2) from queries q2
    where q1.query_name = q2.query_name
    and q2.rating<3
) as poor_query_percentage
from queries q1
group by q1.query_name
having q1.query_name is not null