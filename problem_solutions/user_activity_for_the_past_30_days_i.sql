'''

'''
# Write your MySQL query statement below
SELECT activity_date AS 'day', COUNT(DISTINCT user_id) as 'active_users'
FROM Activity
GROUP BY activity_date
HAVING activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-26'
