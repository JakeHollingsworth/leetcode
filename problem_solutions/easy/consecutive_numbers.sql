'''
Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example.
'''
WITH cte AS (
    SELECT
        LAG(num) OVER (ORDER BY id) AS lagger,
        num,
        LEAD(num) OVER (ORDER BY id) AS leader
    FROM
        Logs
)
SELECT
    DISTINCT num AS "ConsecutiveNums"
FROM
    cte
WHERE 
   lagger = num AND 
   leader = num
