'''
Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

The query result format is in the following example.
'''
# Write your MySQL query statement below
SELECT u.name, CASE WHEN ISNULL(SUM(r.distance)) THEN 0 ELSE SUM(r.distance) END AS 'travelled_distance'
FROM Rides AS r
RIGHT JOIN Users AS u
    ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC
