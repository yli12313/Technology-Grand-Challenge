-- LINK: https://platform.stratascratch.com/coding/10152-workers-with-the-highest-and-lowest-salaries?code_type=3

-- TRICKS:
-- This is a brilliant solution that uses the RANK() function twice with CASE! Doesn't make sense to do 'MAX(salary)' in 
-- the RANK() function when 'MAX(salary)' is not even queried in SELECT! 
-- Really love this solution!
-- When you write code, please come up with short variable names!! This will reduce the amount of syntactical
-- errors that you get when you code!
-- Moreover whenever you use a CASE statement, you should probably assign an alias to the newly created column!
-- Don't forget: CASE statement --> AS <New Column Name>.

with cte1 as (
    select
        worker_id,
        salary,
        department,
        rank() over (order by salary desc) as max_rnk,
        rank() over (order by salary) as min_rnk
    from worker
)

select
    worker_id,
    salary,
    department,
    case
        when max_rnk=1 then "Highest Salary"
        when min_rnk=1 then "Lowest Salary"
    end as salary_type
from cte1
where max_rnk=1 or min_rnk=1;