'''
Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.
'''
SELECT employee_id, CASE WHEN (MOD(employee_id, 2) = 1 AND NOT SUBSTRING(name FROM 1 FOR 1) = 'M') THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id
