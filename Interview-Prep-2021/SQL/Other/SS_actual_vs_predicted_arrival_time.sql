-- LINK: https://platform.stratascratch.com/coding/2135-actual-vs-predicted-arrival-time?code_type=3

-- TRICKS:
-- Extremely tricky problem. First understand that this problem is asking you to return the 90th-percentile
-- value itself, which I didn't understand.
-- Remember that the where clause in the first cte is where you have to restrict the date to: '2022-01-01' and '2022-01-14'.
-- You can do this with either 'predicted_eta' or 'actual_time_of_arrival'.
-- Remember that the ntile(X) window function will partition the dataset into X segments and you can return the
-- value at X segment.
-- To remove duplicate time differences, make sure to use distinct. Forgot to use distinct twice now! Don't forget this!
-- You have to practice more problems like this! They are extremely tricky.

with cte as(
    select 
        abs(timestampdiff(minute, predicted_eta, actual_time_of_arrival)) as time_diff
    from trip_details
    where actual_time_of_arrival between '2022-01-01' and '2022-01-14'
),
cte2 as (
    select
        time_diff,
        ntile(10) over (order by time_diff asc) as rnk
    from cte
)

select 
    distinct time_diff
from cte2
where rnk=9;