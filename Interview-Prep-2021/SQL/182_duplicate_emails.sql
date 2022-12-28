# LINK: https://leetcode.com/problems/customers-who-never-order/

# NOTE: Using a GROUP BY with a HAVING clause with a COUNT operation! Actually
# solved this problem last year, but it's a good practice again. 

SELECT 
    email AS 'Email'
FROM Person
GROUP BY email
HAVING COUNT(email)>=2;