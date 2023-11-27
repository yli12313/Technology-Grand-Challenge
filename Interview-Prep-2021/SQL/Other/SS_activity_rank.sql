-- LINK: https://platform.stratascratch.com/coding/10351-activity-rank?code_type=3

-- TRICKS:
-- Thought that we needed 'rank()' when in reality what we needed was 'row_number()'.
-- The syntax is 'row_number() over (partition by column1 order by column2)'.
-- In this situation, we did an order by in the window function with two differnt columns.
-- There is a group by in the select statement overall.

select 
    from_user,
    count(*) as total,
    row_number() over (order by count(*) desc, from_user asc) as ranking
from google_gmail_emails
group by from_user;
