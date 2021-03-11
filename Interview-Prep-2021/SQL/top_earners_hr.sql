-- LINK: https://www.hackerrank.com/challenges/earnings-of-employees/problem?h_r=internal-search

SELECT 
  months*salary AS earnings,
  COUNT(*)
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;
