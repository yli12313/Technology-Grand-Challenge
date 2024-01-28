-- LINK: https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    distinct a.user_id
from amazon_transactions a
join amazon_transactions b
on a.user_id=b.user_id and a.id <> b.id
where datediff(a.created_at,b.created_at) between 0 and 7
order by a.user_id;
