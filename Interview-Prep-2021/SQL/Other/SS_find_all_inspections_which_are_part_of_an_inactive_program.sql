-- LINK: https://platform.stratascratch.com/coding/10277-find-all-inspections-which-are-part-of-an-inactive-program?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select 
    * 
from los_angeles_restaurant_health_inspections
where program_status='INACTIVE';