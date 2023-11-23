-- LINK: https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?code_type=3

-- TRICK:
-- Super strange problem, but I did it.

select 
    distinct(home_library_code)
from library_usage
where notice_preference_definition="email" and circulation_active_year=2016
and provided_email_address is FALSE;
