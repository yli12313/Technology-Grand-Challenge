-- LINK: https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=3

-- TRICKS:
-- This is a problem where HAVING is useful, because you are filtering on a group by! This is the only
-- time that HAVING is useful so use it sparingly.
-- The DISTINCT is not necessary, but it's nice as a precaution to query only the distinct cities.

select
    distinct city
from zillow_transactions
group by city
having avg(mkt_price) > (select avg(mkt_price) from zillow_transactions);