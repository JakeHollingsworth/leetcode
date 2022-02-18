'''
Write an SQL query to display the records with three or more rows with consecutive ids, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

The query result format is in the following example.
'''
WITH cte AS (
    SELECT
        *,
        LAG(people, 2) OVER (ORDER BY id) AS prevprev,
        LAG(people, 1) OVER (ORDER BY id) AS 'prv',
        LEAD(people, 1) OVER (ORDER BY id) AS 'nxt',
        LEAD(people, 2) OVER (ORDER BY id) AS nextnext
    FROM 
        Stadium
)
SELECT
    id, visit_date, people
FROM 
    cte
WHERE
    people >= 100 AND (
    (prevprev >= 100 AND prv >= 100) OR
    (prv >= 100 AND nxt >= 100) OR
    (nxt >= 100 AND nextnext >= 100)
    )
