-- LINK: https://platform.stratascratch.com/coding/10171-find-the-genre-of-the-person-with-the-most-number-of-oscar-winnings?code_type=3

-- TRICKS:
-- I didn't understand the question. All you want is the genre that has the highest number of Oscar winners; that's it!
-- I didn't know how to use IS: 'where winner is true'.
-- Do not forget that you have to do LIMIT 1 in cte2!
-- I want to practice this one again! I did it!
-- Keep practicing and keep going!

with cte1 as (
    select 
        top_genre,
        name,
        count(distinct nom.id) as num_oscars
    from oscar_nominees nom
    join nominee_information nom_info on nom.nominee=nom_info.name
    where winner is true
    group by name
),
cte2 as (
    select 
        *,
        dense_rank() over (order by count(name) desc) as rnk
    from cte1
    limit 1
)

select 
    top_genre
from cte2;