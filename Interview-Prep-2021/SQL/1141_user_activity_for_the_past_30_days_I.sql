-- LINK: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

-- NOTE: There are two things I want to note about this problem. 
--		 1) The first is that when you use the COUNT function, it's COUNT() with parentheses.
-- 		 2) The second thing I want to note is that I made a small error with the date: 
--		    I put [activity_date>='2019-06-27'] instead of [activity_date>'2019-06-27']. 

--       I'm still not sure how best to eliminate these small errors when I'm programming and 
--       be more precise in my engineering, but I will keep trying and I will keep practicing. 

SELECT
    activity_date AS 'day',
    COUNT(DISTINCT user_id) AS 'active_users'
FROM Activity
WHERE activity_date>'2019-06-27' AND activity_date<='2019-07-27'
GROUP BY activity_date;