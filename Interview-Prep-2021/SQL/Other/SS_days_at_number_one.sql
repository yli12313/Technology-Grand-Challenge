-- LINK: https://platform.stratascratch.com/coding/10173-days-at-number-one?code_type=3

-- TRICKS:
-- Not a hard problem! Didn't know that the primary key here was 'trackname' and 'date'.
-- When the primary keys are the same in the two tables, you can use the USING() function.
-- I just have to keep practicing!

select 
    us.trackname,
    count(us.date) as days_num_one
from spotify_daily_rankings_2017_us us
join spotify_worldwide_daily_song_ranking w using(trackname, date)
group by 1
order by 1;