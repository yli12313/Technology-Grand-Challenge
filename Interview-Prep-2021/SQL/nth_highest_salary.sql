# LINK: https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE cutPoint INT;
  SET cutPoint = N-1;

  RETURN (
      SELECT 
        DISTINCT Salary        
      FROM Employee
      ORDER BY Salary DESC
      LIMIT cutPoint, 1
  );
END