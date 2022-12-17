-- LINK: https://leetcode.com/problems/employees-with-missing-information/

-- NOTE: I learned in this problem that if you want to use HAVING, you have
-- to use GROUP BY first to to aggregate on some field.

SELECT 
    employee_id
FROM
(SELECT * FROM Employees
UNION
SELECT * FROM Salaries) a
GROUP BY employee_id
HAVING COUNT(employee_id) = 1
ORDER BY employee_id;