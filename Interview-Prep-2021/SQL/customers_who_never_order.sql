# LINK: https://leetcode.com/problems/customers-who-never-order/

SELECT c.Name
FROM Customers c
LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL;