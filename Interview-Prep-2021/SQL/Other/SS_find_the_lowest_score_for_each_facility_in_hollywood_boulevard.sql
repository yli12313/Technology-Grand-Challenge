-- LINK: https://platform.stratascratch.com/coding/10180-find-the-lowest-score-for-each-facility-in-hollywood-boulevard?code_type=3

-- TRICKS:
-- This is not even a hard problem! I didn't know how to use the LIKE feature in SQL.
--     "WHERE facility_address LIKE '%HOLLYWOOD_BLVD%'"
-- Moreover in the GROUP BY, you have to GROUP BY 'min(score) AS min_score'. Don't forget this!
-- Yes, MIN() is an aggregation function!
-- Keep practicing and keep going!

select
    min(score) as min_score,
    facility_name
from los_angeles_restaurant_health_inspections
where facility_address like '%HOLLYWOOD_BLVD%'
group by facility_name
order by min_score desc,facility_name;