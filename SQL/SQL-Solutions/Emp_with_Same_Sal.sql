--script:
--CREATE TABLE [emp_salary]
--(
--    [emp_id] INTEGER  NOT NULL,
--    [name] NVARCHAR(20)  NOT NULL,
--    [salary] NVARCHAR(30),
--    [dept_id] INTEGER
--);
--INSERT INTO emp_salary
--(emp_id, name, salary, dept_id)
--VALUES(101, 'sohan', '3000', '11'),
--(102, 'rohan', '4000', '12'),
--(103, 'mohan', '5000', '13'),
--(104, 'cat', '3000', '11'),
--(105, 'suresh', '4000', '12'),
--(109, 'mahesh', '7000', '12'),
--(108, 'kamal', '8000', '11');
--Problem Statement:
/* Write SQL to return all employee whose salary is same in same department*/
with dept_sal as(
    select dept_id,
        salary
    from emp_salary
    group by dept_id,
        salary
    having count(2) > 1
)
select emp_id,
    name
from emp_salary e
    inner join dept_sal d on e.dept_id = d.dept_id
where e.salary = d.salary ----Solution 2
    with dept_sal as(
        select dept_id,
            salary
        from emp_salary
        group by dept_id,
            salary
        having count(2) = 1
    )
select e.*
from emp_salary e
    left join dept_sal d on e.dept_id = d.dept_id
    and e.salary = d.salary
where d.dept_id is null
order by d.dept_id