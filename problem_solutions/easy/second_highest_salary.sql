'''
Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

The query result format is in the following example.
'''
SELECT
    IFNULL(NULL, (
        SELECT
            DISTINCT salary
        FROM 
            Employee
        ORDER BY
            salary DESC
        LIMIT 1
        OFFSET 1   
    )) AS "SecondHighestSalary"
FROM 
    Employee
LIMIT 1
