--INSERT STATEMENT
--create table call_start_logs
--(
--phone_number varchar(10),
--start_time datetime
--);
--insert into call_start_logs values
--('PN1','2022-01-01 10:20:00'),('PN1','2022-01-01 16:25:00'),('PN2','2022-01-01 12:30:00')
--,('PN3','2022-01-02 10:00:00'),('PN3','2022-01-02 12:30:00'),('PN3','2022-01-03 09:20:00')
--create table call_end_logs
--(
--phone_number varchar(10),
--end_time datetime
--);
--insert into call_end_logs values
--('PN1','2022-01-01 10:45:00'),('PN1','2022-01-01 17:05:00'),('PN2','2022-01-01 12:55:00')
--,('PN3','2022-01-02 10:20:00'),('PN3','2022-01-02 12:50:00'),('PN3','2022-01-03 09:40:00')
--;
--Solution 1
with all_calls as (
    (
        select phone_number,
            ROW_NUMBER() OVER(
                PARTITION BY phone_number
                order by start_time
            ) as rn,
            start_time as call_time
        from call_start_logs s
    )
    union all
    select phone_number,
        ROW_NUMBER() OVER(
            PARTITION BY phone_number
            order by end_time
        ) as rn,
        end_time
    from call_end_logs e
)
select phone_number,
    rn,
    min(call_time) as start_time,
    max(call_time) as end_time
from all_calls
group by phone_number,
    rn