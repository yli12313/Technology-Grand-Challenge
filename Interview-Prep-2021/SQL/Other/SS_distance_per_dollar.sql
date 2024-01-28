-- LINK: https://platform.stratascratch.com/coding/10302-distance-per-dollar?code_type=3

-- TRICKS:
-- This was just not a good problem overall; super tricky problem that took me a while to solve.
-- But I guess it's good practice you know?
-- One thing to remember about the DISTINCT keyword is that you can only apply it to columns that
-- are categorical. This is something to keep in mind of.
-- Don't forget 'DISTINCT ym' when you do this problem!
-- Basically this problem wants you to find 'dist_per_dollar' and 'avg_dist_per_dollar' and do a cal-
-- culation with it.

with cte1 as (
select 
    request_date,
    date_format(request_date,'%Y-%m') as ym,
    sum(distance_to_travel)/sum(monetary_cost) as dist_per_dollar,
    avg(sum(distance_to_travel)/sum(monetary_cost)) over (partition by date_format(request_date,'%Y-%m')) as avg_dist_per_dollar
from uber_request_logs
group by request_date
)

select 
    distinct ym,
    round(abs(dist_per_dollar-avg_dist_per_dollar), 2) as abs_avg_difference
from cte1
order by request_date