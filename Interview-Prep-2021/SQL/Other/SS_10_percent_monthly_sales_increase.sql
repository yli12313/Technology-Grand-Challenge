-- LINK: https://platform.stratascratch.com/coding/2157-10-monthly-sales-increase?code_type=3

-- TRICKS:
-- Be careful with the names of the ctes.
-- The syntax of the CASE statement is: CASE WHEN ... THEN ... ELSE ... END.
-- Make sure that you are querying in the following order:
-- 1) The first cte queries from the original table.
-- 2) The second cte queries from the first cte.
-- 3) The last select statement queries from the second cte.
-- When doing SQL just like Python/Leetcode, write out the skeleton of the code first.

with monthly_sales as (
    select 
        product_id,
        sum(case when month(date)=4 then (cost_in_dollars*units_sold) else 0 end) as april_sales,
        sum(case when month(date)=5 then (cost_in_dollars*units_sold) else 0 end) as may_sales
    from online_orders
    group by product_id

),
percent_increase as (
    select
        product_id,
        ((may_sales-april_sales)/april_sales)*100 as percent
    from monthly_sales
)

select
    product_id,
    percent
from percent_increase
where percent>=10;