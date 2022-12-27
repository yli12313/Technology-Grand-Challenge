-- LINK: https://leetcode.com/problems/top-travellers/

-- NOTE: Note you can GROUP BY one column and choose another column to be
-- displayed. It's pretty interesting.

SELECT 
    u.name,
    CASE 
        WHEN SUM(distance) != 0 THEN SUM(distance)
        ELSE 0
    END AS 'travelled_distance'
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, name ASC;