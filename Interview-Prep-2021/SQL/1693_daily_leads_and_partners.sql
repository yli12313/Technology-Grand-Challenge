-- LINK: https://leetcode.com/problems/daily-leads-and-partners/

-- NOTE: Solved this SQL problem. Have faith and confidence in yourself when you
-- are doing anything technical. So what if you fail and don't get things working
-- correctly the first time; get up and try again!

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS 'unique_leads',
    COUNT(DISTINCT partner_id) AS 'unique_partners'
FROM DailySales
GROUP BY date_id, make_name