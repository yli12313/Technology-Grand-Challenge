# LINK: https://leetcode.com/problems/trips-and-users/

# NOTE: Keep going and keep practicing!
    
select
    request_at as Day,
    round(
        count(if(status in ('cancelled_by_driver', 'cancelled_by_client'), 1, null))
        / count(*)
    , 2) as 'Cancellation Rate'
from Trips
where client_id
    in (select users_id from Users where banned = 'No')
    and driver_id
    in (select users_id from Users where banned = 'No')
GROUP BY request_at
having request_at between '2013-10-01' and '2013-10-03'
