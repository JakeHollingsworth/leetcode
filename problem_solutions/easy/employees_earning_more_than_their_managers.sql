SELECT
    e.name AS "Employee"
FROM 
    Employee AS e
LEFT JOIN 
    Employee AS m ON
    e.managerId = m.id
WHERE
    e.salary > m.salary
