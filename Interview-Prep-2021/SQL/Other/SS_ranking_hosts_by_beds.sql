-- LINK: https://platform.stratascratch.com/coding/10161-ranking-hosts-by-beds?code_type=3

-- TRICKS:
-- Not a hard problem, but please find out the difference between COUNT() and SUM() in MySQL!
-- The trick to doing these problems is to outline the problem first!
-- Moreover, see if you need a cte from the beginning; don't have the intuition yet to know
-- when you need a cte or not.
-- I suggest try solving the problem with a single query first. If you can't do that then you
-- bring in a cte.

select
    host_id,
    sum(n_beds) tot_num_beds,
    dense_rank() over (order by sum(n_beds) desc) as rnk
from airbnb_apartments
group by host_id;