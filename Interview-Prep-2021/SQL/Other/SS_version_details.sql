-- LINK: https://platform.stratascratch.com/coding/9913-order-details?code_type=3

-- TRICKS:
-- When doing an order by, the ordering is already ascending so you don't need to write 'ASC'!
-- You can simplify the where clause; see version 2!

-- Version 1:
/*select 
    order_date,
    order_details,
    total_order_cost,
    first_name
from customers c
JOIN orders o ON c.id = o.cust_id
WHERE first_name="Jill" OR first_name="Eva"
ORDER BY cust_id ASC;*/

-- Version 2:
select 
    order_date,
    order_details,
    total_order_cost,
    first_name
from customers c
JOIN orders o ON c.id = o.cust_id
WHERE first_name IN ("Jill","Eva")
ORDER BY cust_id ASC;
