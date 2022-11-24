'''
Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The query result format is in the following example.
'''
# Write your MySQL query statement below
SELECT DISTINCT author_id as 'id'
FROM Views AS v1
WHERE author_id = viewer_id
ORDER BY author_id ASC
