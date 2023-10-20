-- LINK: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3
-- TRICKS:
-- 1) Make sure you have the correct id for the department table 'department_id'.
-- 2) Make sure you have insightful names for each table!
-- 3) Make sure that you actually select 'MAX(salary)' from each of the subqueries!

SELECT ABS(
(SELECT MAX(salary) 
FROM db_employee emp 
JOIN db_dept dept ON emp.department_id = dept.id 
WHERE department = "marketing")
-
(SELECT MAX(salary) 
FROM db_employee emp 
JOIN db_dept dept ON emp.department_id = dept.id 
WHERE department = "engineering")) AS salary_diff;
