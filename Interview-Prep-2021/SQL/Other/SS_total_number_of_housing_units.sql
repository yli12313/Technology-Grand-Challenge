-- LINK: https://platform.stratascratch.com/coding/10167-total-number-of-housing-units?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    year,
    sum(south+west+midwest+northeast) as units_completed
from housing_units_completed_us
group by year
order by year;