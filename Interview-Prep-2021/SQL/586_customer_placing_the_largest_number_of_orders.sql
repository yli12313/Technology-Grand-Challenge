-- LINK: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

-- NOTE: I didn't know about [ORDER BY COUNT(*) DESC] when you do a GROUP BY. Now
-- I do. Moreover, if you need to select a specific row from a table, your mind should
-- think about the LIMIT clause immediately!

SELECT
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;