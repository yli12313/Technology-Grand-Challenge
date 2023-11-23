-- LINK: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3

-- TRICKS:
-- Make sure to remember that you can do a subquery in the where clause! 
-- Example: 'where salary in (<subquery>)'.

select
    worker_title
from worker w
join title t on w.worker_id=t.worker_ref_id
where salary in (
select 
    max(salary)
from worker
);
