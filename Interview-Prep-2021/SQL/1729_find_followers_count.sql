-- LINK: https://leetcode.com/problems/find-followers-count/

-- NOTE: Very easy problem, but it's good practice you know? Always be careful w.r.t. 
-- the ORDER BY clause. 

SELECT
    user_id,
    COUNT(follower_id) AS 'followers_count'
FROM Followers
GROUP BY user_id
ORDER BY user_id;