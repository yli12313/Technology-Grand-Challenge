-- LINK: https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=3

-- TRICKS:
-- You actually don't need 'as' when you are giving a column an alias.
-- When you are doing a join of two tables, any column header with a column that is uniquely
-- only in one table can be referenced by it's name. 
-- For notation purposes, it's a good idea to include which column is coming from
-- which table.
-- Don't always assume you are joining on the two primary keys of two different tables! In 
-- this join operation, we are joining 'a.user_id = b.id'.

-- Solution with more notation, but is more readable
select
    b.id,
    b.name,
    sum(a.distance) as tot_distance
from lyft_rides_log a
join lyft_users b on a.user_id=b.id
group by b.id
order by tot_distance desc
limit 10;

-- Solution that has less notation, but is less readable
-- select
--     b.id,
--     name,
--     sum(distance) total_distance
-- from lyft_rides_log
-- inner join lyft_users b on user_id = b.id
-- group by b.id
-- order by total_distance desc
-- limit 10;