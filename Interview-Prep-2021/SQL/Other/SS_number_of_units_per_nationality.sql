-- LINK: https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=3

-- TRICKS:
-- Had all the logic right except for "count(distinct unit_id)", which is ok!
-- You have to always think that when you use COUNT(), do you want to count DISTINCT?
-- You almost always need to do 'COUNT(DISTINCT <column>)'.
-- You are doing great!

select
    nationality,
    count(distinct unit_id) as num_apartments
from airbnb_hosts h
join airbnb_units u using(host_id)
where unit_type="Apartment" and age < 30
group by nationality
order by num_apartments desc;