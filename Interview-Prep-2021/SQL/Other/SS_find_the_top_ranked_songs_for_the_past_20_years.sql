-- LINK: https://platform.stratascratch.com/coding/10283-find-the-top-ranked-songs-for-the-past-30-years?code_type=3

-- TRICKS:
-- Don't forget to use DISTINCT!
-- You can use 'YEAR(CURRENT_DATE)' to get the current year!
-- Keep practicing and keep going!

-- Hard coded solution:
-- select 
--     distinct song_name
-- from billboard_top_100_year_end
-- where year_rank=1 and year between 2004 and 2024;

-- More dynamic solution:
select 
    distinct song_name
from billboard_top_100_year_end
where year_rank=1 and year(current_date)-year <= 20;