-- LINK: https://platform.stratascratch.com/coding/10313-naive-forecasting?code_type=3

-- This was not a hard problem. I had it all right and the logic down. 
-- IMPORTANT: if you do an order by in the first cte, you don't need to do an order by in the
-- window finction in the second cte, as long as you are NOT using partition by! But it's still 
-- good convention to add the order by in the window function.
-- I just didn't know that square in MySQL is implemented as: pow(<expr>, <to the ith power>).

with cte1 as (
select
    month(request_date) as month,
    sum(distance_to_travel) / sum(monetary_cost) as dpd
from uber_request_logs
group by month
order by month
),
cte2 as (
    select 
        month, 
        dpd,
        lag(dpd,1) over (order by month) as previous_dpd 
    from cte1
)

select
    round(sqrt(avg(pow(dpd-previous_dpd, 2))),2) as rmse
from cte2;