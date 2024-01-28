-- LINK: https://platform.stratascratch.com/coding/9988-find-the-top-3-jobs-with-the-highest-overtime-pay-rate?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select
    jobtitle
from sf_public_salaries
order by overtimepay desc
limit 3;