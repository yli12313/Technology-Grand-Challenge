-- LINK: https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=3

-- TRICKS:
-- This was not a hard problem, but I just made some mistakes. I didn't realize that you should
-- use the SUM() function here and that when you pair it with the CASE statement, the THEN clause
-- should not be 1, but should be the actual variable 'downloads' itself!
-- Be careful with respect to when you should use SUM() vs. when you should use COUNT(). Still need
-- to develop intuition on that. But I will get better with more practice!
-- Moreover, I can optimize the code by using the function USING() and the HAVING clause.
-- Lastly, when you have a table that is used to separate a M:M relationship among two other tables,
-- never start the join chain with the auxiliary table that breaks the M:M relationship!
-- I'm going to practice this problem again! I was able to successfully workout the optimized
-- solution.

-- Original solution
/* with cte1 as (
select 
    date,
    sum(case when paying_customer='no' then downloads else 0 end) as non_paying,
    sum(case when paying_customer='yes' then downloads else 0 end) as paying
from ms_download_facts mdf
join ms_user_dimension mud on mdf.user_id=mud.user_id
join ms_acc_dimension mad on mud.acc_id=mad.acc_id
group by date
)

select 
    *
from cte1
where non_paying > paying
order by date */

-- Optimized solution
select
    date,
    sum(case when paying_customer='no' then downloads else 0 end) as not_paying,
    sum(case when paying_customer='yes' then downloads else 0 end) as paying
from ms_download_facts mdf
join ms_user_dimension mud using(user_id)
join ms_acc_dimension mad using(acc_id)
group by date
having not_paying>paying
order by date;