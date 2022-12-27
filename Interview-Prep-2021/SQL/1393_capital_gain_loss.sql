-- LINK: https://leetcode.com/problems/capital-gainloss/

-- NOTE: Very nice solutions that involved some googling! You did this with an
-- a SUM(IF()), where you applied two functions. The way that the IF() statement
-- operates is IF(condition, branch1 [True], branch2 [False]). It's a little bit
-- easier than the CASE statement.  

SELECT
    stock_name,
    SUM(IF(operation='Buy', -price, price)) AS 'capital_gain_loss'
FROM Stocks
GROUP BY stock_name;