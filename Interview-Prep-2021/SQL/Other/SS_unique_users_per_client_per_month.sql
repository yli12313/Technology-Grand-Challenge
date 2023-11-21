-- LINK: https://platform.stratascratch.com/coding/2024-unique-users-per-client-per-month?code_type=3

-- TRICKS:
-- If you redefine a column name in the select clause and need to group by that column, you can 
-- use the NEW COLUMN NAME in the group by clause.

select 
    client_id as client,
    month(time_id) as month,
    count(distinct(user_id)) as users
from fact_events
group by month, client_id
