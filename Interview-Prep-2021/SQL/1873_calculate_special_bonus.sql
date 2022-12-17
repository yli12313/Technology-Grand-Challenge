-- LINK: https://leetcode.com/problems/calculate-special-bonus/

SELECT
    e.employee_id,
    CASE
        WHEN e.employee_id % 2 = 1 AND LEFT(e.name, 1) != 'M' THEN e.salary
        ELSE 0
    END AS 'bonus'
FROM Employees e
ORDER BY e.employee_id;