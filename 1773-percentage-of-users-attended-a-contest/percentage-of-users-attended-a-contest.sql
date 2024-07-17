with total_users as (
    select count(*) as cnt from users
)

select r.contest_id, round(count(distinct r.user_id)*100/t.cnt,2) as percentage from register r, total_users t
group by r.contest_id
order by percentage desc,r.contest_id