select * from tasks;
drop table tasks;

create table tasks(
    id serial primary key,
    task_id integer,
    task_name varchar(50),
    task varchar(1000),
    task_date varchar(30),
    status boolean
);

truncate table tasks restart identity;

alter table tasks
alter column task_name set data type varchar(100);