'''
Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.

Return the result table in any order.

The query result format is in the following example.
'''
# Write your MySQL query statement below
WITH tbl AS (
    SELECT user_id, time_stamp
    FROM Logins
    WHERE YEAR(time_stamp) = 2020
)
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM tbl
GROUP BY user_id
