-- LINK: https://leetcode.com/problems/rank-scores/

SELECT 
  Score AS score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS `Rank`
FROM Scores;
