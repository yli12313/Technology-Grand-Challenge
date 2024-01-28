-- LINK: https://platform.stratascratch.com/coding/10301-expensive-projects?code_type=3

-- TRICKS: 
-- Not a hard problem, only thing is that you needed 'budget' and not 'sum(budget)'!
-- Keep practicing and keep going!

select 
    title,
    round(budget/count(emp_id)) as budget_per_employee
from ms_projects a
join ms_emp_projects b on a.id=b.project_id
group by id
order by budget_per_employee desc;