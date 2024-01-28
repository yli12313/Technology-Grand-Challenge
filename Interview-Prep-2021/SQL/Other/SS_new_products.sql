-- LINK: https://platform.stratascratch.com/coding/10318-new-products?code_type=3

-- TRICKS:
-- Had the right idea, just didn't know that when using COUNT() with the CASE statement, the COUNT()
-- operation has to wrap the CASE statement.
-- You don't need to do 'ELSE NULL' because it's already NULL by default.
-- Don't forget that you have to do 'group by company_name' in the cte.
-- Keep practicing and keep going!

with cte1 as (
select 
    company_name,
    count(case when year='2019' then product_name end) as products_2019,
    count(case when year='2020' then product_name end) as products_2020
from car_launches
group by company_name
)

select 
    company_name,
    products_2020-products_2019 as net_difference
from cte1;