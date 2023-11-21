-- LINK: https://platform.stratascratch.com/coding/2119-most-lucrative-products?code_type=3

-- TRICKS:
-- When you want to find something that's between two intervals, you can use the 'where' clause with
-- 'between..and'.
-- Example: 'where month(date) between 1 and 6'.

select 
    product_id,
    sum(cost_in_dollars*units_sold) as total_revenue
from online_orders
where month(date) between 1 and 6
group by product_id
order by total_revenue desc
limit 5;
