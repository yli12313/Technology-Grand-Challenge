-- LINK: https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=3

-- TRICKS:
-- Have to read the questions more carefully! 
-- You have to group by the 'bike_number'!
-- Because you have done a group by operation, you have to then select the 'MAX(end_time)'!
-- Yes, when you do the order by operation, you have to add 'DESC' to have the most recently used at the top!

select
bike_number,
MAX(end_time)
from dc_bikeshare_q1_2012
GROUP BY bike_number
ORDER BY end_time DESC;
