-- LINK: https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=3

-- TRICKS:
-- You have to really understand the problem to be able to write the 'WHERE' clause!

SELECT
    event_name,
    COUNT(*) AS event_count
FROM playbook_events
WHERE device = "macbook pro"
GROUP BY event_name
ORDER BY event_count DESC;
