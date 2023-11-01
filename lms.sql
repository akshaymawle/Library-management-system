create database lms; 
use lms;
select* from vehicle;
create table books(book_id varchar (255),
book_name varchar (255),
author_name varchar (255),
primary key (book_id));
#inserting  rows
insert into books values("2000","intro to python","Akshay");
insert into books values("2001","intro to c","Akshay");
insert into books values("2002","intro to java","Akshay");

select * from books
books
update books set book_name="intro to economy" where book_id="2000";

delete from books where book_id="2002";

create table users(
users_id varchar (255) primary key,
users_pwd varchar (255)
);

insert into  users values("akshay97@library.com","Akshay123");
insert into users values("avi@16library.com","Avi2151");
insert into users values("aarush22@librarycom","Aarush22");
insert into users values("avani10@library.com","Avani10");
insert into users values("akashshikare","akash")

select * from users;

update users set users_id="akshay@97library.com" where users_id="akshay7@library.com";

delete from users where users_id="akshay@97library.com";

create table admins(
admins_id varchar (255) primary key,
admins_pwd varchar (255)
);

insert into admins values("kajal14@library.com","Akash@114");
select * from admins;
create table issue(
issue_id varchar (255) primary key,
book_id varchar (255),
users_id  varchar (255)
);

 select * from issue;
 
 drop table users;
 
 create table users(
users_id varchar (255) primary key,
users_pwd varchar (255)
);

insert into  users values("akshay97@library.com","Akshay123");
insert into users values("avi@16library.com","Avi2151");
insert into users values("aarush22@librarycom","Aarush22");
insert into users values("avani10@library.com","Avani10");

select * from users;
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY '1234';
drop table admina;
select * from car;