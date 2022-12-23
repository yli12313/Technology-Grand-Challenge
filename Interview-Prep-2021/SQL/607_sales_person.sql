-- LINK: https://leetcode.com/problems/sales-person/

-- NOTE: For a problem such as this one, you really have to understand what you are
-- joining and in what order! I thought that the problem was a triple left join problem,
-- but in reality the problem was a subquery problem. The structure of the SQL statement
-- is very important as you work through these problems. Maybe drawing things out on a 
-- piece of paper could help a lot in the problem solving phase!

SELECT
    sp.name AS 'name'
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
SELECT
    o.sales_id
FROM Orders o
LEFT JOIN Company c
ON o.com_id=c.com_id
WHERE c.name='RED'
)