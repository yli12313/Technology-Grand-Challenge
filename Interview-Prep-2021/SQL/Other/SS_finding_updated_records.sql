-- LINK: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=3

-- TRICKS:
-- You have to include the 'DISTINCT id' values; otherwise you get duplicate rows.
-- The syntax for the window function is: 'MAX(salary) OVER (PARTITION BY id) AS salary'.

select 
    DISTINCT id,
    first_name,
    last_name,
    department_id,
    MAX(salary) OVER (PARTITION BY id) AS salary
from ms_employee_salary
ORDER BY id;
