-- LINK: https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=3

-- TRICKS:
-- Pretty tricky problem. Didn't know about the ROWS clause. The syntax of this clause is:
--    ROWS BETWEEN .. AND ..
-- Make sure to remember that it's ROWS and not ROW!
-- Otherwise this problem is fine, a normal cte problem followed by a subsequent query. I'm
-- seriously running out of energy right now. But I have to keep it up. You are doing great!
-- Keep practicing and keep going!

with cte1 as (
    select 
        date_format(created_at, '%Y-%m') as ym,
        sum(purchase_amt) as total_amt
    from amazon_purchases
    where purchase_amt > 0
    group by ym
    order by ym
)

select
    ym,
    avg(total_amt) over (order by ym rows between 2 preceding and current row) as rolling_avg
from cte1;