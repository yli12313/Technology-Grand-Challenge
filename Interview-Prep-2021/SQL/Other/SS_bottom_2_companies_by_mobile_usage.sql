-- LINK: https://platform.stratascratch.com/coding/2026-bottom-2-companies-by-mobile-usage?code_type=3

-- TRICKS:
-- Pretty good man! You are getting better so keep going. 
-- With this one just remember that in sql, comparison is done using the single '=' operator.
-- Once again, remember that when you do order by, the clause is already sorted by 'asc'.
-- Yes, MySQL does have the COUNT() aggregate function!
-- Don't forget that the 'customer_id' is the primary key here! You are doing group by on
-- 'customer_id'!
-- Forgot to filter out client_id for only records that have 'mobile'.

with cte1 as (
    select
        customer_id,
        count(client_id) as cnt
    from fact_events
    where client_id='mobile'
    group by customer_id
),
cte2 as (
    select
        customer_id,
        cnt,
        dense_rank() over (order by cnt) as rnk
    from cte1
),

select
    customer_id,
    cnt
from cte2
where rnk <= 2;