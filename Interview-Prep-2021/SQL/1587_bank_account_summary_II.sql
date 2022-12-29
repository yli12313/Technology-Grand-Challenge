-- LINK: https://leetcode.com/problems/bank-account-summary-ii/

-- NOTE1: In this problem, I used the WHERE clause when I should have been using
-- the HAVING clause. After I applied the SUM() function and casted the new column
-- as 'balance', I could no longer use 'balance' in the WHERE clause, but I could
-- use it in the HAVING clause. The difference between WHERE and HAVING is:

-- A HAVING clause is like a WHERE clause, but applies only to groups as a whole 
-- (that is, to the rows in the result set representing groups), whereas the WHERE
-- clause applies to individual rows. A query can contain both a WHERE clause and a
-- and a HAVING clause. 

SELECT
    u.name,
    SUM(t.amount) AS 'balance'
FROM Users u
LEFT JOIN Transactions t
ON u.account=t.account
GROUP BY u.name
HAVING balance > 10000;

-- NOTE2: When you do a subquery where the subquery is in the FROM clause, you
-- have to give the subquery an alias. I always seem to forget that!

-- Unoptimal solution with a subquery.
-- SELECT
--     a.name,
--     a.balance
-- FROM (
-- SELECT
--     name,
--     SUM(amount) AS 'balance'
-- FROM Users u
-- LEFT JOIN Transactions t
-- ON u.account=t.account
-- GROUP BY name) a
-- WHERE a.balance>10000;