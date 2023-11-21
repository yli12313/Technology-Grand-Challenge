-- https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains/solutions?code_type=3

-- TRICKS:
-- This is the first time I've used 'like'.
-- The syntax is: 'where <column> like "<exp>"'.
-- You can use the '%' character inside "<exp>" to match zero, one or more characters.
-- You can use the '_' character inside "<exp>" to match one, single characters.

select 
    employeename,
    basepay
from sf_public_salaries
where jobtitle like "%captain%";
