-- LINK: https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=3

-- TRICKS:
-- Good problem; not much of an issue with this one!

select 
    artist,
    count(id) as total_appearances
from spotify_worldwide_daily_song_ranking
group by artist
order by total_appearances desc;
