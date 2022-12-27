-- LINK: https://leetcode.com/problems/find-total-time-spent-by-each-employee/

-- NOTE: This problem is interesting. It's a double GROUP BY. Watch out for problems when it's 
-- a double group by.

SELECT 
    event_day AS 'day',
    emp_id,
    SUM(out_time-in_time) AS 'total_time'
FROM Employees
GROUP BY event_day, emp_id;