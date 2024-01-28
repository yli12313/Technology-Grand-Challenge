-- LINK: https://platform.stratascratch.com/coding/10358-friday-purchases?code_type=3

-- TRICKS: 
-- I had a lot of problems with this one.
-- The functions that I didn't know how to use: WEEK(), AVG(), WEEKDAY(), IFNULL(), QUARTER().

-- CTE:
-- You have to select 'week(date)' and group by it in the cte.
-- You have to grab the average of the amount spent.
-- You have to check that 'weekday(date)' is 4.

-- Second SELECT statement:
-- You have to remember that you are now selecting from the original table joined to the cte! 
-- 'avg_amount' is the only thing that you are querying from the cte, so it's not 'amount_spent'.
-- You are selecting from the original table and doing a left join with the cte.
-- For some reason you have to do 'week(date)=cte1.week_number'. I have no idea why, but you do.
-- Don't forget to use DISTINCT and IFNULL() in this part of the code!

with cte1 as (
    select 
        week(date) as week_number,
        avg(amount_spent) as avg_amount
    from user_purchases
    where weekday(date)=4
    group by week_number
)

select 
    distinct week(date) as week_number,
    ifnull(avg_amount,0) as mean_amount
from user_purchases a
left join cte1 on week(date)=cte1.week_number
where quarter(date)=1;