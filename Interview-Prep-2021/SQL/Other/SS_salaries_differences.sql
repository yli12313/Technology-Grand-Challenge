-- LINK: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3

SELECT ABS(
(SELECT max(salary) 
FROM db_employee emp 
JOIN db_dept dept ON emp.department_id = dept.id 
WHERE department = "marketing")
-
(SELECT max(salary) 
FROM db_employee emp 
JOIN db_dept dept ON emp.department_id = dept.id 
WHERE department = "engineering")) AS salary_diff;
