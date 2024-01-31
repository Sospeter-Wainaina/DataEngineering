--INSERT STATEMENT
--create table input (
--id int,
--formula varchar(10),
--value int
--)
--insert into input values (1,'1+4',10),(2,'2+1',5),(3,'3-2',40),(4,'4-1',20);
--Solution
with cte as (
    select *,
        left(formula, 1) as id1,
        right(formula, 1) as id2,
        substring(formula, 2, 1) as sign
    from input
)
select c.formula,
    i1.value as value_1,
    i2.value as value_2,
    case
        when c.sign = '+' then (i1.value + i2.value)
        when c.sign = '-' then (i1.value - i2.value)
    end as result
from cte c
    inner join input i1 on c.id1 = i1.id
    inner join input i2 on c.id2 = i2.id