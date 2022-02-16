SELECT
    name AS "Customers"
FROM 
    Customers c
LEFT JOIN 
    Orders o ON
    c.id = o.customerId
WHERE 
    ISNULL(o.id)
