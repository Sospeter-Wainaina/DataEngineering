--create table tickets
--(
--ticket_id varchar(10),
--create_date date,
--resolved_date date
--);
--delete from tickets;
--insert into tickets values
--(1,'2022-08-01','2022-08-03')
--,(2,'2022-08-01','2022-08-12')
--,(3,'2022-08-01','2022-08-16');
--create table holidays
--(
--holiday_date date
--,reason varchar(100)
--);
--delete from holidays;
--insert into holidays values
--('2022-08-11','Rakhi'),('2022-08-15','Independence day');
/* Write an sql to find the business day between create date and resolved date by excluding
 weekends ad public holidays
 --2022-08-01 -> Monday , --2022-08-03 -> Wednesday
 --2022-08-01 -> Monday , --2022-08-12 -> Friday
 --2022-08-01 -> Monday , --2022-08-03 -> Tuesday
 */
--SOLUTION
with actual_business_days as (
    select *,
        datediff(Day, create_date, resolved_date) as actual_days,
        --datediff(week,create_date,resolved_date) as week_diff,
        datediff(Day, create_date, resolved_date) - datediff(week, create_date, resolved_date) * 2 as business_days
    from tickets t
        left join holidays h on h.holiday_date between t.create_date and t.resolved_date
)
select ticket_id,
    create_date,
    resolved_date,
    datediff(Day, create_date, resolved_date) - datediff(week, create_date, resolved_date) * 2 - count(holiday_date) as actual_business_days
from actual_business_days
group by ticket_id,
    create_date,
    resolved_date