SELECT prod.id, prod.name, prod.isbn, prod.company_id, prod.price, comp.name AS company_name
FROM products prod
LEFT JOIN companies comp ON prod.company_id = comp.id;