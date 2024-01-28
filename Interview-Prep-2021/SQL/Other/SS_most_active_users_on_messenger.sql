-- LINK: https://platform.stratascratch.com/coding/10295-most-active-users-on-messenger?code_type=3

-- TRICKS:
-- Forgot how to use UNION ALL! The two tables that are being joined have to have the same columns to
-- do UNION ALL. Moreover if two corresponding columns have different column names, caste them such that
-- they have the same column names!
-- Don't forget to do UNION ALL when you write the code itself!
-- Moreover, yes you can join ctes together like you do normal tables in MySQL!

with cte1 as (
    select user1 as user, msg_count from fb_messages
    union all
    select user2 as user, msg_count from fb_messages
)

select 
    user,
    sum(msg_count) as tot_messages
from cte1
group by user
order by tot_messages desc
limit 10;