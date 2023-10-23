-- LINK: https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=3

-- TRICKS:
-- This was not a hard problem; just have to read the problem!

SELECT
    location,
    AVG(popularity)
FROM facebook_employees emp
JOIN facebook_hack_survey surv 
ON emp.id = surv.employee_id
GROUP BY location;
