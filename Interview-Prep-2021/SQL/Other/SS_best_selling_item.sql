-- LINK: https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=3

-- TRICKS:
-- I was on the right track, but I was not totally there on this one. 
-- I still have problems knowing when I should use COUNT() vs. when I should use SUM(). I have to develop
-- better intuition by practicing more.
-- You have to GROUP BY 'month(invoicedate)' and 'description'.
-- I get the window function now! You are doing a 'dense_rank()' with the clauses:
--     1) 'PARTITION BY MONTH(invoicedate)'
--     2) 'ORDER BY SUM(unitprice*quantity) DESC'
-- Moreover, 'MONTH(invoicedate)' and 'SUM(unitprice*quantity)' are two other columns that you've selected
-- from the SELECT statement!
-- Keep practicing and keep going!

with cte1 as (
    select
        month(invoicedate) as each_month,
        description,
        sum(unitprice*quantity) as best_selling_item,
        dense_rank() over (partition by month(invoicedate) order by sum(unitprice*quantity) desc) as rnk
    from online_retail
    group by 1,2
)

select
    each_month,
    description,
    best_selling_item
from cte1
where rnk=1;