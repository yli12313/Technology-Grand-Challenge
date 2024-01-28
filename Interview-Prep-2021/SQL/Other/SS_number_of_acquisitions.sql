-- LINK: https://platform.stratascratch.com/coding/10162-number-of-acquisitions?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    acquired_quarter,
    count(id) as acquisition_count
from crunchbase_acquisitions
group by acquired_year,acquired_quarter
order by acquisition_count desc;