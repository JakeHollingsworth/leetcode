'''
Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

The query result format is in the following example.
'''
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
          DISTINCT salary
      FROM 
          Employee
      ORDER BY
          salary DESC
      LIMIT 1
      OFFSET M
  );
END
