-- LINK: https://platform.stratascratch.com/coding/9962-top-10-qbs?code_type=3

-- TRICKS:
-- You did not understand the problem here! All the problem is asking for you to get is the 
-- top 10 quarterback-rating pairs. The same quarterback can appear twice in the final answer! 
-- Therefore, you don't need 'partition by qb' or 'group by qb'.
-- Always go with the simpler choice when it comes to programming. 'rnk' is better than `rank`.
-- The key point to remember is that: you are starting StrataScratch again and you are rusty, that's
-- all! There's nothing wrong with your skills.
-- It's just that you have not practiced in a few weeks. 

-- My solution
-- with ratings as (
--     select 
--         qb,
--         rate,
--         dense_rank() over (order by rate desc) as rnk
--     from qbstats_2015_2016
-- )

-- select 
--     qb,
--     rate
-- from ratings
-- where rnk between 1 and 10;

-- Optimized solution
select
    qb,
    rate
from qbstats_2015_2016
order by rate desc
limit 10;