-- LINK: https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=3

-- TRICKS:
-- Learned this new syntax: "avg(timestampdiff(second,a.t,b.t)".
-- For the two subqueries, you need to group by two columns: 'user_id', "date(timestamp)".
-- For each user, you have to isolate the latest 'page_load' or 'page_entry' time by date.
-- You need to find the last average session time of the day.
-- You have two subqueries, but you need a group by for the top query too!

select a.user_id,avg(timestampdiff(second,a.t,b.t)) as avg
from
(select
    user_id,
    max(timestamp) as t
from facebook_web_log
where action="page_load"
group by user_id,date(timestamp)) a
join
(select
    user_id,
    max(timestamp) as t
from facebook_web_log
where action="page_exit"
group by user_id,date(timestamp)) b
on a.user_id=b.user_id
group by 1;
