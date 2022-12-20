-- LINK: https://leetcode.com/problems/second-highest-salary/

-- NOTE: For SOLUTION 1, you cannot use MAX(salary) in the WHERE clause!
-- You have to use the field name itself, not someFunction(fieldName). For
-- SOLUTION 2, it solves the issue of only having one record in the table. I
-- have no idea why it does this, but it does lol.

-- SOLUTION 1
SELECT
    MAX(salary) AS 'SecondHighestSalary'
FROM Employee
WHERE salary != (SELECT MAX(salary) FROM Employee);


-- SOLUTION 2
SELECT (SELECT
    DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1,1) AS 'SecondHighestSalary'