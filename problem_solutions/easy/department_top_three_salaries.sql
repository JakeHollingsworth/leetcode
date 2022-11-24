'''
A companys executives are interested in seeing who earns the most money in each of the companys departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write an SQL query to find the employees who are high earners in each of the departments.

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
    rnk <= 3
