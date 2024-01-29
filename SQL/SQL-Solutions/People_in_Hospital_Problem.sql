--create table hospital ( emp_id int
--, action varchar(10)
--, time datetime);
--insert into hospital values ('1', 'in', '2019-12-22 09:00:00');
--insert into hospital values ('1', 'out', '2019-12-22 09:15:00');
--insert into hospital values ('2', 'in', '2019-12-22 09:00:00');
--insert into hospital values ('2', 'out', '2019-12-22 09:15:00');
--insert into hospital values ('2', 'in', '2019-12-22 09:30:00');
--insert into hospital values ('3', 'out', '2019-12-22 09:00:00');
--insert into hospital values ('3', 'in', '2019-12-22 09:15:00');
--insert into hospital values ('3', 'out', '2019-12-22 09:30:00');
--insert into hospital values ('3', 'in', '2019-12-22 09:45:00');
--insert into hospital values ('4', 'in', '2019-12-22 09:45:00');
--insert into hospital values ('5', 'out', '2019-12-22 09:40:00'
--Solution
-- Write an SQL to find the total number of people present in the hospital
select *
from (
        select emp_id,
            action,
            row_number() over(
                partition by emp_id
                order by time desc
            ) as latest
        from hospital
    ) a
where a.latest = 1
    and action = 'in'