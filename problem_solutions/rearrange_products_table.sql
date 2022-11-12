'''
Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The query result format is in the following example.
'''
# Write your MySQL query statement below
WITH s1 AS (
    SELECT product_id, 'store1' AS store, store1 AS price
    FROM Products
    WHERE NOT ISNULL(store1)
), s2 AS (
    SELECT product_id, 'store2' AS store, store2 AS price
    FROM Products
    WHERE NOT ISNULL(store2)
), s3 AS (
    SELECT product_id, 'store3' AS store, store3 AS price
    FROM Products
    WHERE NOT ISNULL(store3)
)

SELECT * FROM s1
UNION ALL
SELECT * FROM s2
UNION ALL
SELECT * FROM s3
