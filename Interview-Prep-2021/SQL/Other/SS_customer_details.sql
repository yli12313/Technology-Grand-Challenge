-- LINK: https://platform.stratascratch.com/coding/9891-customer-details?code_type=3

-- TRICK:
-- Have to just keep practicing the syntax for joins! It's <JOIN> [TABLE] <ON> [CONDITION].

-- Version 1:
/*
SELECT
    first_name,
    last_name,
    city,
    order_details
FROM customers c
LEFT JOIN orders o ON c.id = o.cust_id
ORDER BY first_name,order_details;
*/

-- Version 2:
SELECT
    first_name,
    last_name,
    city,
    order_details
FROM customers c
LEFT JOIN orders o ON c.id = o.cust_id
ORDER BY 1,4;
