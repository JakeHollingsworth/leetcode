'''

Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in any order.

The query result format is in the following example.
'''
# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users AS u
JOIN Transactions AS t
    ON u.account = t.account
GROUP BY u.account 
HAVING SUM(amount) > 10000
