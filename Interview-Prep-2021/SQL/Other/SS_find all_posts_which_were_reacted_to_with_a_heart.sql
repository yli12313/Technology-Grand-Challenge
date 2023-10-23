-- LINK: https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=3

-- TRICKS:
-- Have to make sure you have 'DISTINCT' in the query!
-- The subquery solution is actually simpler so think how you can solve these problems with subqueries sometimes please!

-- Version 1 (Using a JOIN):
/*SELECT
    DISTINCT(posts.post_id),
    posts.poster,
    posts.post_text,
    posts.post_keywords,
    posts.post_date
FROM facebook_posts posts
JOIN facebook_reactions react
ON posts.post_id = react.post_id
WHERE reaction="heart";*/

-- Version 2 (Using subquery):
SELECT *
FROM facebook_posts
WHERE post_id IN (
SELECT post_id
FROM facebook_reactions
WHERE reaction="heart"
);
