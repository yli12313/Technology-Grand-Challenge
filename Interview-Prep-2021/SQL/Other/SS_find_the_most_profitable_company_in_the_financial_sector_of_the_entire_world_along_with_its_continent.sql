-- LINK: https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=3

-- TRICKS:
-- To get better at using the 'having' clause, keep using it!
-- It's important to note that by default, the order by clause is 'ASC'. To get 'DESC', you have
-- to define it!

select 
    company,
    continent
from forbes_global_2010_2014
where sector="financials"
having max(profits);
