-- LINK: https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT e.Name AS Employee
FROM Employee e, Employee m
WHERE e.ManagerId = m.Id
  AND e.Salary > m.Salary;