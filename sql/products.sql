create table if not exists products (
       id int not null primary key auto_increment,
       name varchar(100) not null,
       category varchar(10) not null
)
