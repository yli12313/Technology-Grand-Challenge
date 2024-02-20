-- LINK: https://platform.stratascratch.com/coding/10169-highest-total-miles?code_type=3

-- TRICK:
-- Keep practicing and keep going!

with cte1 as (
    select 
        purpose,
        sum(miles) as total_miles
    from my_uber_drives
    where category="Business"
    group by purpose
    order by total_miles desc
)

select
    purpose,
    total_miles
from cte1
limit 3;