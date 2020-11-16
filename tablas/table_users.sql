create table users(
    id serial primary key,
    user_name varchar(50),
    password varchar(100),
    init_date varchar(30),
    email varchar(100)
);

truncate table users restart identity;

alter table users
drop column rol;

select * from users;

alter table users
alter column password set data type varchar(100);

delete from users where id = 3;