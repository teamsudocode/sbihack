create table users (
       user_id int not null primary key auto_increment,
       cif_number varchar(20) not null,
       creation_time timestamp not null default current_timestamp
)
