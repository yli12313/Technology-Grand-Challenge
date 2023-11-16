-- LINK: https://platform.stratascratch.com/coding/10003-lyft-driver-wages?code_type=3

-- TRICKS:
-- There was a glitch as I was trying to submit this problem.
-- To select all the columns, your immediate thought should be to use "*"!

select 
    l.index,
    l.start_date,
    l.end_date,
    l.yearly_salary
from lyft_drivers l
where l.yearly_salary <= 30000 or l.yearly_salary >= 70000;
