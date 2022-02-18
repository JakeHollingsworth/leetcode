'''
Write an SQL query to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The query result format is in the following example.
'''
WITH cte AS (
    SELECT
        *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM 
        Employee
)
SELECT
    d.name AS "Department", 
    e.name AS "Employee", 
    e.salary AS "Salary"
FROM 
    cte AS e
JOIN
    Department AS d ON
    e.departmentId = d.id
WHERE 
    rnk = 1
