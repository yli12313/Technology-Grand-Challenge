-- LINK: https://platform.stratascratch.com/coding/10166-reviews-of-hotel-arena?code_type=3

-- TRICK:
-- SQL is not hard at all; you just need to consistently practice everyday!

SELECT 
    hotel_name,
    reviewer_score,
    COUNT(reviewer_score) AS score_count
FROM hotel_reviews
WHERE hotel_name = "Hotel Arena"
GROUP BY reviewer_score
