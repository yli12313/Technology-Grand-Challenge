# LINK: https://leetcode.com/problems/department-highest-salary/

SELECT
  t.Department,
  t.Employee,
  t.Salary
FROM
(SELECT
  d.Name AS Department,
  e.Name AS Employee,
  e.Salary AS Salary,
  RANK() OVER (PARTITION BY d.Name ORDER BY Salary DESC) as r
FROM Employee e
JOIN Department d ON e.DepartmentId=d.Id) t
WHERE t.r = 1;