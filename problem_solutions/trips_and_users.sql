'''
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The query result format is in the following example.
'''
WITH cte AS (
    SELECT 
        t.request_at,
        CASE
            WHEN t.status ='cancelled_by_client' OR t.status='cancelled_by_driver' THEN 1
            ELSE 0
        END AS cancelled
    FROM Trips AS t
    LEFT JOIN
        Users AS c ON
        c.users_id = t.client_id
    LEFT JOIN
        Users AS d ON
        d.users_id = t.driver_id
    WHERE
        d.banned = 'No' AND 
        c.banned = 'No' AND
        t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)

SELECT 
    request_at as "Day", 
    ROUND(SUM(cancelled) / COUNT(cancelled), 2) AS 'Cancellation Rate'
FROM 
    cte
GROUP BY
    request_at
