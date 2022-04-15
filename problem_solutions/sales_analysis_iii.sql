'''
Write an SQL query that reports the products that were only sold in the spring of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

The query result format is in the following example.
'''
SELECT p.product_id, p.product_name
FROM Sales AS s
JOIN Product AS p
    ON s.product_id = p.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= "2019-01-01" AND MAX(s.sale_date) <= "2019-03-31" 
