-- LINK: https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    cust_id,
    first_name,
    sum(total_order_cost) as total_order_cost
from customers c
join orders o on c.id=o.cust_id
group by cust_id
order by first_name;