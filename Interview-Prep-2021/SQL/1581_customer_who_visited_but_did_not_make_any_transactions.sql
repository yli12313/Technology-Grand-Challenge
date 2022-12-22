-- LINK: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

-- NOTE: When you cast a field such as creating the 'count_no_trans', you can
-- use it on another clause such as ORDER BY.

SELECT 
    v.customer_id,
    COUNT(v.customer_id) AS 'count_no_trans'
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id=t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id
ORDER BY count_no_trans DESC;