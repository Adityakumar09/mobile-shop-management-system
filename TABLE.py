import mysql.connector as sql
c=sql.connect(host='localhost',user='root',passwd='9205',database='mobile')
c1=c.cursor()
c1.execute("create table mobile(phone_code int primary key not null ,phone_name varchar(45) not null  ,brand varchar(20) not null ,stock_available int not null,cost_price int not null ,selling_price int not null )")
c1.execute("create table customer(gmail_id varchar(40) primary key not null,phone_code int not null,customer_name varchar(25) not null ,phone_name varchar(30) not null ,date_of_purchase varchar(14) not null,selling_price int not null,quantity int not null ,amount_paid int not null ,mode_of_payment varchar(20) not null,customer_number varchar(10) not null,customer_address varchar(45) not null , PROFIT int )")
print("successfully created ")
