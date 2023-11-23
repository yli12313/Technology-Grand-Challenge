-- LINK: https://platform.stratascratch.com/coding/9847-find-the-number-of-workers-by-department?code_type=3

-- TRICK:
-- None!

select 
    department,
    count(worker_id) as num_workers
from worker
where month(joining_date)>=4
group by department
order by num_workers desc;
