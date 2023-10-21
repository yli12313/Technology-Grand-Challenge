-- LINK: https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=3

-- TRICKS:
-- We are told: "Find the average number of bathrooms and bedrooms for each city’s property types."
-- This means we have to do a GROUP BY operation with 'city,property_type'!

SELECT
    city,
    property_type,
    AVG(bathrooms) AS avg_bathrooms,
    AVG(bedrooms) AS avg_bedrooms
FROM airbnb_search_details
GROUP BY city,property_type;
