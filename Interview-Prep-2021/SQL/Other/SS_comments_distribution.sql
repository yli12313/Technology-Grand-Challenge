-- LINK: https://platform.stratascratch.com/coding/10297-comments-distribution?code_type=3

-- TRICKS:
-- This is not a hard problem overall. Except that the only thing that was tricky was the way
-- that the problem was worded. 
-- You are getting the users and a count of the number of comments they made.
-- Then you are getting the counts and the number of users that made that number of comments.
-- Don't think this was a hard problem, but it's just worded extremely tricky and hard to 
-- comprehend. Therefore, you have to practice it again!
-- FYI: HAVING is not the right place to select rows. That should be in the WHERE clause. 
-- One thing about typing SQL is that maybe it's better to type the conditions first? I'm
-- not sure, so I'm going to keep practicing.

with cte1 as (
    select 
        c.user_id,
        count(body) as count_comments
    from fb_users u
    join fb_comments c on u.id = c.user_id
    where c.created_at >= u.joined_at and
    c.created_at between '2020-01-01' and '2020-01-31' and
    year(u.joined_at) between 2018 and 2020
    group by c.user_id
)

select count_comments, count(user_id)
from cte1
group by count_comments
order by count_comments;