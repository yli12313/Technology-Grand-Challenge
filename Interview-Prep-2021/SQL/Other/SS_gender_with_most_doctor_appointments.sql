-- LINK: https://platform.stratascratch.com/coding/10170-gender-with-most-doctor-appointments?code_type=3

-- TRICKS:
-- Take your time! Be careful with the implementation!
-- Forgot to do a 'desc'. You just need to slow down and don't get frustrated when you get an error!

select 
    gender,
    count(appointmentid) as doc_appointments
from medical_appointments
group by gender
order by doc_appointments desc
limit 1;