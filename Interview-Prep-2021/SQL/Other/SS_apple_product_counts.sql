-- LINK: https://platform.stratascratch.com/coding/10141-apple-product-counts?code_type=3

-- TRICKS:
-- IMPORTANT: In StrataScratch, the order of the columns is not important in a SELECT statement. The
-- more important thing is to get the logic right!
-- Extremely tricky problem. Remember you are inner joining: 'playbook_users' <--> 'playbook_events'.
-- To join two tables, you can use USING() if the primary/foreign key of the two tables have the same
-- name. 
-- Using, COUNT, DISTINCT, and CASE together is extremely tricky! I need to practice more.
-- When writing out the CASE statement, always write out the skeleton first! Don't forget to include 'end'.

select 
    language,
    count(distinct case when b.device in ('macbook pro','iphone 5s','ipad air') then a.user_id else NULL end) as users_dev,
    count(distinct a.user_id) as tot_users
from playbook_users a
join playbook_events b using(user_id)
group by language
order by tot_users desc;