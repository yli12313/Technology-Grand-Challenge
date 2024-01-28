-- LINK: https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3

-- TRICKS:
-- This was a good problem with lots of tricks. Remember that if you want to format the date, you can use
-- DATE_FORMAT().
-- Yes, if you order by a column in the window function, you don't have to do it at the end of the query.
-- However if you use order by in the window function, please do not use any column aliases!
-- You are querying the following in the cte: the year-month, the revenue from the last month, and the 
-- revenue from the current month.

with cte1 as (
    select 
        date_format(created_at, "%Y-%m") as ym,
        sum(value) as rev_month,
        lag(sum(value),1) over (order by date_format(created_at, "%Y-%m")) as rev_next_month
    from sf_transactions 
    group by ym
)

select
    ym,
    round(((rev_next_month-rev_month) / rev_month)*100, 2) as percent_change
from cte1;