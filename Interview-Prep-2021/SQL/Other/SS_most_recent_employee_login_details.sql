-- LINK: https://platform.stratascratch.com/coding/2141-most-recent-employee-login-details?code_type=3

select *
from worker_logins
where login_timestamp in (
    select 
        max(login_timestamp)
    from worker_logins
    group by worker_id
)
