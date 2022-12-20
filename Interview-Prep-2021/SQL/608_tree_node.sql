-- LINK: https://leetcode.com/problems/tree-node/

-- NOTE: I am getting better at SQL. This problem has given me a lot of confidence.

SELECT 
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS 'type'
FROM Tree