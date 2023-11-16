-- LINK: https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=3

-- TRICKS:
-- Read the problem carefully!
-- If stuck ask ChatGPT before looking at the answers!

SELECT 
    COUNT(movie) AS nominations
FROM oscar_nominees
WHERE nominee = "Abigail Breslin";
