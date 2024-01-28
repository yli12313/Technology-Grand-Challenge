-- LINK: https://platform.stratascratch.com/coding/10160-rank-guests-based-on-their-ages?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select
    guest_id,
    rank() over (order by age desc) as rnk
from airbnb_guests;