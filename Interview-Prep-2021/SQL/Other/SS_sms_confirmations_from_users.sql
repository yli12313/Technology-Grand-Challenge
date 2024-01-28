-- LINK: https://platform.stratascratch.com/coding/10291-sms-confirmations-from-users?code_type=3

-- TRICKS:
-- This is a left join problem where a smaller table is being joined to a bigger table.
-- In this situation, you do all the calculations based on the bigger table. Don't forget this!
-- Need to have more intuition as to when you should use LEFT JOIN and when you should use INNER JOIN.
-- Also didn't see that the key that you should use to join the two tables together is both the
-- <date> and also the <phone number>.
-- Lastly, when you calculate the percentage, you have to multiply by 100.
-- Don't forget that this is a left join problem!

select
    count(c.phone_number)/count(ss.phone_number)*100 as percentage
from fb_sms_sends ss
left join fb_confirmers c on ss.ds=c.date and ss.phone_number=c.phone_number
where ss.ds='2020-08-04' and ss.type='message';

