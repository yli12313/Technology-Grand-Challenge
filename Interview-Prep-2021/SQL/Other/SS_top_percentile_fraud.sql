-- LINK: https://platform.stratascratch.com/coding/10303-top-percentile-fraud?code_type=3

-- TRICKS:
-- This was a tricky problem that I did not do correctly nor have the right intuition in knowing
-- what tools to use to solve the problem.
-- This problem did not want you to group by the states; it wanted you to use a window function
-- to find 'the top 5 percentile of claims for each state.' This is where you have to do
-- 'partition by state' in the SQL function. Once again, you are not aggregating by state.
-- Rather you want to partition by each state and find the top 5 percent of claims for that state.
-- This is where you should use 'percent_rank()'. Moreover in this current implementation where you 
-- have 'order by fraud_score desc', the result of the 'percent_rank()' is in ascending order 
-- where: "value X is in the top Y percent". Therefore to find the top 5%, the operation would 
-- be 'percentile <= .05'.

-- If fraud_score desc --> then 'percentile <= .05'.
-- If fraud_score asc --> then 'percentile >= .95'.

-- Make sure to read the problem carefully to know whether you need to use 'partition by' or not!

with cte1 as (
select 
    policy_num,
    state,
    claim_cost,
    fraud_score,
    percent_rank() over (partition by state order by fraud_score desc) as percentile
from fraud_score
)

select 
    policy_num,
    state,
    claim_cost,
    fraud_score
from cte1
where percentile <= .05