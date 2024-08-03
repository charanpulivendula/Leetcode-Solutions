# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(SubString(name,1,1)),Lower(SubString(name,2,LENGTH(name)))) as name
FROM Users
ORDER BY user_id