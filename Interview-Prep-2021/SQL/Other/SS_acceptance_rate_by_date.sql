-- LINK: https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=3

-- TRICKS:
-- I'm still not sure why you have to group by 'user_id_sender' for this problem. I guess the reason is 
-- because you can send/accept multiple friend requests a day? You have to group by the person first
-- and then group by the date. This is not obvious from reading the problem statement so ALWAYS make sure
-- you understand the problem first before you start coding!!
-- This is a situation where you are using COUNT() first in the cte and then SUM() in the query that
-- follows the cte.
-- Let me just try writing this one out again. I finally did it. This was a hard problem for me.
-- When you use COUNT(), you can actually use '1' instead of the variable name if you want.

with cte1 as (
    select
        user_id_sender,
        date,
        count(case when action='accepted' then 1 end) as accepted,
        count(case when action='sent' then 1 end) as sent
    from fb_friend_requests
    group by user_id_sender
)

select
    date,
    sum(accepted)/sum(sent) as percentage
from cte1
group by date
order by date;