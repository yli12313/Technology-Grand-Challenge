-- LINK: https://leetcode.com/problems/market-analysis-i/

-- NOTE: When you are joining you have to visualize the tables as you are doing the join
-- mentally. This is something that I'm still working on and that I need to improve. I had a
-- mental image of what I was joining, but it was wrong. Need to practice. Also, learned the
-- difference between SUM and COUNT:

-- +----+------+
-- | id | vote |
-- +----+------+
-- |  1 |    1 |
-- |  2 |   -1 |
-- |  3 |    1 |
-- |  4 |   -1 |
-- |  5 |    1 |
-- +----+------+

-- COUNT = 5 votes

-- SUM = 1 vote
-- (-2 + 3 = 1)

-- I was thinking about COUNT for this problem when I should have been thinking about SUM! Need
-- to practice more I guess overall; but it's ok, I will get there! :)

SELECT 
    u.user_id AS 'buyer_id',
    u.join_date,
    SUM(IF(YEAR(o.order_date)=2019, 1, 0)) AS 'orders_in_2019'
FROM Users u
LEFT JOIN Orders o
ON u.user_id=o.buyer_id
GROUP BY u.user_id;