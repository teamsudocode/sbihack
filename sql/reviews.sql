create table if not exists reviews (
  id int not null auto_increment primary key,
  submission_time timestamp not null default current_timestamp,
  product_id int not null,
  user_id int not null,
  rating numeric(2, 1) not null check (rating>=0 and rating<=5),
  comment varchar(255)
);
