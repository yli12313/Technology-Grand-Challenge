-- LINK: https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=3

-- TRICKS:
-- Always understand the problem first before you start writing code!
-- Keep practicing and keep going!

select 
    dense_rank() over (order by sum(n_messages) desc) as rnk,
    id_guest,
    sum(n_messages) as tot_messages
from airbnb_contacts
group by id_guest;