-- LINK: https://platform.stratascratch.com/coding/9917-average-salaries?code_type=3

-- TRICKS: 
-- No notes to record with this one; good problem!
-- Make sure to have good variable names and be confidence with the variable names that you choose!

SELECT
    department,
    first_name,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg_salary
FROM employee e
