-- LINK: https://leetcode.com/problems/article-views-i/

-- HINT: Make sure to always check what you need to ORDER BY when you are 
-- doing SQL!

SELECT
    DISTINCT author_id AS 'id'
FROM Views
WHERE author_id=viewer_id
ORDER BY 1;