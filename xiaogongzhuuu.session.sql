SELECT*FROM message;
use fastapi;
show tables;
create table product(
	id int primary key auto_increment,
    name varchar(255) not null,
    price int not null default 20
);

insert into product(id, name, price) values(1,'汉堡',50);
insert into product(id, name, price) values(2,'热狗',30);
insert into product(id, name, price) values(3,'奶茶',20);
insert into product(name) values("果汁");
select * from product;
select price,name from product where price>20;

set sql_safe_updates=0;
update product set price=50 where name="奶茶";
update product set name="果茶",price=25 where name="奶茶";
update product set price=30 where price <= 35;

delete from product where name="果茶";


drop table product;


    