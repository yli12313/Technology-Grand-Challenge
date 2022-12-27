-- LINK: https://leetcode.com/problems/the-latest-login-in-2020/

-- NOTE: The condition in the WHERE clause is 'YEAR(time_stamp)=2020'. I didn't 
-- know about the YEAR() function. I guess that you have to be extra careful with 
-- the WHERE clause because 'WHERE time_stamp >= 2020-01-01 AND time_stamp >= 2020-12-31'
-- didn't work for me!

SELECT
    user_id,
    MAX(time_stamp) AS 'last_stamp'
FROM Logins
WHERE YEAR(time_stamp)=2020
GROUP BY user_id;