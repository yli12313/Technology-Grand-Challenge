-- LINK: https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3

-- TRICK:
-- The solution using the window function: 'rank() over (order by profits desc) as company_ranked'
-- is super interesting!
-- When you have a subquery, the outer query needs to assign a name to the subquery!

-- ## Version 1 ##
-- select
--     company,
--     profits as highest_profits
-- from forbes_global_2010_2014
-- order by highest_profits desc
-- limit 3;

-- ## Version 2 ##
select
    company,
    profits
from (
select
    company,
    profits,
    rank() over (order by profits desc) as company_ranked
from forbes_global_2010_2014
) as ranked
limit 3;
