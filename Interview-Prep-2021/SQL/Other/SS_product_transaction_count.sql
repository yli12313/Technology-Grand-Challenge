-- LINK: https://platform.stratascratch.com/coding/10163-product-transaction-count?code_type=3

-- TRICKS:
-- Keep practicing and keep going!

select 
    product_name,
    count(transaction_id) as num_transactions
from excel_sql_transaction_data a
join excel_sql_inventory_data b using(product_id)
group by product_name
order by a.product_id;