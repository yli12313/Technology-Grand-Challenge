-- LINK: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

-- NOTE: This was an easy problem, but it was good practice with 
-- a double GROUP BY.

SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(director_id) >= 3;