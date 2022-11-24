'''
Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The query result format is in the following example.
'''
SELECT
    CASE
        WHEN MOD(id, 2) = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        WHEN MOD(id, 2) = 1 THEN id + 1
        ELSE id - 1 
    END AS id,
    student
FROM
    Seat
ORDER BY
    id ASC
