-- LINK: https://platform.stratascratch.com/coding/2142-third-heaviest-package?code_type=3

-- TRICKS: 
-- IMPORTANT: When you are unsure what the table looks like, first do a query to check!
-- IMPORTANT: When you are doing a window function, the key word to remember is 'over'!
-- You have to include 'desc' in the window function because the heaviest weight has rank 1.
-- You have to do 'group by shipment_id' because each shipment_id has multiple items that's
-- being shipped. Do not forget the 'group by shipment_id' part!
-- With the cte syntax, do not for get 'as'!
-- When you define a cte: make sure to use the cte's name in subsequent queries, and not the 
-- original table's name!

with shipment_ranking as (
    select 
        shipment_id,
        sum(weight) as total_weight,
        dense_rank() over (order by sum(weight) desc) as `rank`
    from amazon_shipment
    group by shipment_id
)

select 
    shipment_id,
    total_weight
from shipment_ranking
where `rank`=3;