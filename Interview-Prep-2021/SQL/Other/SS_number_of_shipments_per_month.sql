-- LINK: https://platform.stratascratch.com/coding/2056-number-of-shipments-per-month?code_type=3

-- TRICKS:
-- You learned how to use the 'date_format()' function.
-- When you are enumerating columns in a select statement, don't forget the ',' after each column!
-- You learned how to use the 'month()' function.

select 
    date_format(shipment_date, "%Y-%m") as shipment_date,
    count(shipment_id) as number_per_month
from amazon_shipment
group by month(shipment_date);
