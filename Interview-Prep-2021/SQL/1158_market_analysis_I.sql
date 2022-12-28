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

-------

-- For the query:
-- SELECT 
--     *
-- FROM Users u
-- LEFT JOIN Orders o
-- ON u.user_id=o.buyer_id;

-- You get the table shown below:
-- | user_id | join_date  | favorite_brand | order_id | order_date | item_id | buyer_id | seller_id |
-- | ------- | ---------- | -------------- | -------- | ---------- | ------- | -------- | --------- |
-- | 1       | 2018-01-01 | Lenovo         | 2        | 2018-08-02 | 2       | 1        | 3         |
-- | 1       | 2018-01-01 | Lenovo         | 1        | 2019-08-01 | 4       | 1        | 2         |
-- | 2       | 2018-02-09 | Samsung        | 6        | 2019-08-05 | 2       | 2        | 4         |
-- | 2       | 2018-02-09 | Samsung        | 3        | 2019-08-03 | 3       | 2        | 3         |
-- | 3       | 2018-01-19 | LG             | 5        | 2018-08-04 | 1       | 3        | 4         |
-- | 4       | 2018-05-21 | HP             | 4        | 2018-08-04 | 1       | 4        | 2         |

-- We want to keep the values within the year 2019, but we also don't want to remove the values that are not
-- in 2019, i.e. user_id 3 and 4. Therefore, the WHERE clause is not appropriate for this use case right here.

SELECT 
    u.user_id AS 'buyer_id',
    u.join_date,
    SUM(IF(YEAR(o.order_date)=2019, 1, 0)) AS 'orders_in_2019'
FROM Users u
LEFT JOIN Orders o
ON u.user_id=o.buyer_id
GROUP BY u.user_id;
