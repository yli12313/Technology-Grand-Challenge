-- LINK: https://leetcode.com/problems/rearrange-products-table/description/

-- NOTE: Simple problem, I thought too much with regard to this problem. What
-- I should have done was start working on the problem right away. It was a
-- simple problem that involved SELECT, UNION. I over-thought the problem! Next
-- time I will start right away. :)

SELECT 
    product_id,
    'store1' AS 'store',
    store1 AS 'price'
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT
    product_id,
    'store2' AS 'store',
    store2 AS 'price'
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT
    product_id,
    'store3' AS 'store',
    store3 AS 'price'
FROM Products
WHERE store3 IS NOT NULL