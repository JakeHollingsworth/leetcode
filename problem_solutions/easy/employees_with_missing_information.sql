'''
Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employees name is missing, or
The employees salary is missing.
Return the result table ordered by employee_id in ascending order.

The query result format is in the following example.
'''

SELECT u.employee_id
FROM (
    SELECT e.employee_id
    FROM Employees AS e
    UNION
    SELECT s.employee_id
    FROM Salaries AS s
) AS u
LEFT JOIN Employees AS ee 
    ON u.employee_id = ee.employee_id
LEFT JOIN Salaries AS ss 
    ON u.employee_id = ss.employee_id
WHERE ee.name IS NULL OR ss.salary IS NULL
ORDER BY u.employee_id ASC 
