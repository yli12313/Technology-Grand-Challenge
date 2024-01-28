-- LINK: https://platform.stratascratch.com/coding/10355-employees-with-same-birth-month?code_type=3

-- TRICKS:
-- I had the right idea, but didn't have the implementation down!
-- You can use the CASE WHEN ... THEN ... ELSE ... END statement to define new columns in the resulting
-- query.
-- You have to do 'group by profession' in the second query because the group by in the cte is 
-- 'group by profession,birth_month'. You need the second group by operation to drill down to just an
-- aggregation of 'profession'.

with cte as (
select
    profession,
    birth_month,
    count(employee_id) as cnt
from employee_list
group by profession,birth_month
)

select
    profession,
    sum(case when birth_month=1 then cnt else 0 end) as month_1,
    sum(case when birth_month=2 then cnt else 0 end) as month_2,
    sum(case when birth_month=3 then cnt else 0 end) as month_3,
    sum(case when birth_month=4 then cnt else 0 end) as month_4,
    sum(case when birth_month=5 then cnt else 0 end) as month_5,
    sum(case when birth_month=6 then cnt else 0 end) as month_6,
    sum(case when birth_month=7 then cnt else 0 end) as month_7,
    sum(case when birth_month=8 then cnt else 0 end) as month_8,
    sum(case when birth_month=9 then cnt else 0 end) as month_9,
    sum(case when birth_month=10 then cnt else 0 end) as month_10,
    sum(case when birth_month=11 then cnt else 0 end) as month_11,
    sum(case when birth_month=12 then cnt else 0 end) as month_12
from cte
group by profession;