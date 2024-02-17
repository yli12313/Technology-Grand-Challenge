-- LINK: https://platform.stratascratch.com/coding/10184-order-all-countries-by-the-year-they-first-participated-in-the-olympics?code_type=3

-- TRICKS: 
-- Not a hard problem at all! Forgot to use 'MIN()'. Moreover, whenever you use GROUP BY you should be 
-- using some kind of aggregation function.
-- Also make sure you are ordering by 'min(year)'! This will make the result look nicer.
-- Keep practicing and keep going!

select
    noc,
    min(year) as year
from olympics_athletes_events
group by noc
order by year,noc;