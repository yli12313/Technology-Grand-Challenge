-- LINK: https://platform.stratascratch.com/coding/9845-find-the-number-of-employees-working-in-the-admin-department?code_type=3

-- TRICK:
-- None!

select 
    count(worker_id) as number_of_employees
from worker
where department="admin" and month(joining_date)>=4
