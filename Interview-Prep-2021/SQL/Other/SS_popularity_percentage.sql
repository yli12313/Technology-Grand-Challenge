-- LINK: https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=3

-- TRICKS:
-- Super rusty after three weeks of not doing any SQL on StrataScratch. Now I need to get
-- back to where I was.
-- First you have to get 'user1' and 'user2' together using UNION ALL. It doesn't matter that
-- there are duplicates.
-- Then you have to calculate the 'popularity percentage'. Count the friends that a user has 
-- and then get the total number of Meta users using the following syntax: 
--     "SELECT COUNT(DISTINCT <column>) FROM <table>"
-- Remember: this is a subquery! It will produce the same number everytime!
-- Don't forget that when you are calculating the 'popularity percentage', you have to multiply
-- by 100!
-- You have to GROUP BY and ORDER BY 'users'.
-- This is the first problem you have done in three weeks. You are a bit rusty and that's ok!

with cte1 as (
    select user1 as users from facebook_friends
    union all
    select user2 as users from facebook_friends
)

select
    users,
    count(*) / (select count(distinct users) from cte1)*100 as popularity_percentage
from cte1
group by users
order by users;