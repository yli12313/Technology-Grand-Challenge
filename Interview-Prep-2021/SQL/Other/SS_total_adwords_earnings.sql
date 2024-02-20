-- LINK: https://platform.stratascratch.com/coding/10164-total-adwords-earnings?code_type=3

-- TRICK:
-- Keep practicing and keep going!

select
    business_type,
    sum(adwords_earnings) as tot_earnings
from google_adwords_earnings
group by business_type;