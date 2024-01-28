-- LINK: https://platform.stratascratch.com/coding/10187-find-the-total-number-of-available-beds-per-hosts-nationality?code_type=3

-- TRICKS:
-- You need to use SUM() instead of COUNT(), don't forget this!
-- Keep practicing and keep going!

select 
    nationality,
    sum(n_beds) as tot_avail_beds
from airbnb_hosts a
join airbnb_apartments b using(host_id)
group by nationality;