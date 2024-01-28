-- LINK: https://platform.stratascratch.com/coding/10304-risky-projects?code_type=3

-- TRICKS: 
-- Pretty tricky problem with lots of moving pieces! I got the join right, but was stuck
-- on some of the logic to implement the whole solution.
-- You needed a cte to calculate the 'prorated_salary' field, and then you need a second query 
-- to query the 'prorated_salary' field. This was something that I did not see. I also did not 
-- see the piece of logic that gives you the answer: 'prorated_salary > project_budget'.
-- Moreover, I had trouble with the 'prorated_salary' logic.
-- This idea of calculating a new field and then getting a second query to query the new field
-- is something that I need to practice more (i.e. ctes and subqueries).
-- Keep practicing and keep going!

with cte1 as (
select 
    title,
    budget as project_budget,
    ceiling(sum(datediff(end_date,start_date)/365*salary)) as prorated_salary
from linkedin_projects lp
join linkedin_emp_projects lep on lp.id=lep.project_id
join linkedin_employees le on lep.emp_id=le.id
group by title
)

select 
    title,
    project_budget,
    prorated_salary
from cte1
where prorated_salary > project_budget;