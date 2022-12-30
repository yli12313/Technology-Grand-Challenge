-- LINK: https://leetcode.com/problems/sales-analysis-iii/

-- NOTE: This was a hard problem, but I learned a few things while doing it. I had to look at an 
-- answer, but I did learn a lot.

-- 1) The HAVING clause is after the GROUP BY clause; I had the order confused at one point.
-- 2) You can used the BETWEEN clause as follows: 'WHERE column_name BETWEEN value1 AND value2'.
-- 3) I messed up and used an AND instead of an OR in the WHERE clause of the subquery. You have
--    to be extra careful with WHERE statement conditions, and not take any mental shortcuts.
-- 4) For this problem, doing an INNER JOIN vs. LEFT JOIN yielded the same result.

-- This was a pretty hard problem overall and I had to spend some time really thinking about it.
-- I'm also not mentally fresh right now, and that could have contributed to why I was not able 
-- to finish the work faster. When doing engineering/coding work, it just makes things so much
-- more effective when you can think clearly!

SELECT 
    p.product_id, 
    product_name
FROM Product p 
INNER JOIN Sales s
ON p.product_id=s.product_id
WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31' 
and p.product_id NOT IN (
    SELECT product_id FROM Sales
    WHERE sale_date<'2019-01-01' OR sale_date > '2019-03-31'
)
GROUP BY p.product_id;