-- LINK: https://leetcode.com/problems/consecutive-numbers/

SELECT
  num,
  COUNT(*) OVER (PARTITION BY num) AS ConsecutiveNums
FROM Logs;