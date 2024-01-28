-- LINK: https://platform.stratascratch.com/coding/10350-algorithm-performance?code_type=3

-- TRICKS:
-- This is one of the most important questions that I've solved so far! Solving this hard problem 
-- has given me A LOT of confidence.
-- Yes, in a CASE statement, you can use AND in any of the condition statements.
-- When doing a CASE statement, you have to use CASE..END at the beginning and the end. In the middle,
-- you can have as many WHEN..THEN.. operations as you want.
-- You can only use one ELSE in the CASE statement and you do not have to use it. If none of the 
-- conditions are met and you do not have an ELSE clause, the CASE statement will return NULL.

with cte as (
select 
    search_id, 
    case 
        when clicked <= 0 then 1 
        when clicked > 0 and search_results_position > 3 then 2
        when clicked > 0 and search_results_position <= 3 then 3
        else 0 
    end as rating
from fb_search_events
)

select
    search_id,
    max(rating) as highest_rating
from cte
group by search_id;