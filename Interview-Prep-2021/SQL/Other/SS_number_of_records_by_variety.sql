-- LINK: https://platform.stratascratch.com/coding/10168-number-of-records-by-variety?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    variety,
    count(variety) as num_of_records
from iris
group by variety
order by variety;