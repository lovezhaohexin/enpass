#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(
     host= '127.0.0.1',
     port=3306,
     user='root',
     password='123456',
     db='nsd1809',
     charset='utf8'
)

curser = conn.cursor() #创建游标,类似于文件对象,用来执行sql 语句


# create_department = '''create table department(
# dep_id int , dep_name varchar(20) not NULL UNIQUE,
# primary key(dep_id)) 
# 
# '''
# curser.execute(create_department)
#
# create_employees = '''create table employees(
# emp_id int,emp_name varchar(20),gender varchar(6),
# birth_date date,email varchar(50),dep_id int,
# primary key(emp_id),
# FOREIGN KEY (emp_id) REFERENCES department(dep_id))
# '''
#
# curser.execute(create_employees)

# create_salary ='''create table salary(
# auto_id int,emp_id int,date DATE ,basic int,awards int,
# PRIMARY KEY(auto_id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )'''
# curser.execute(create_salary)
# insert_dep1 = 'insert into department(dep_id,dep_name) values(%s,%s)'
#
# curser.executemany(insert_dep1,[(4,'财务部'),(5,'运动不'),(6,'人才不')])
# insert_emp1 = 'insert into employees values(%s,%s,%s,%s,%s,%s) '
#
# curser.executemany(
#     insert_emp1,
#     [
#         (1,'肉肉','男','1996-1-1','h@tedu.com',2),
#         (2,'垃圾','女','1996-2-2','z@qq.com',3),
#
#     ]
# )
# curser.executemany()
# query_dep1 = 'select * from department order by dep_id'
# curser.execute(query_dep1)
# result1 = curser.fetchone()
# print(result1)
# print('*'*30)
# result2 = curser.fetchmany(1)
# print(result2)
# print('*'*30)
# result3 = curser.fetchall()
# print(result3)
# print('*'*30)
# curser.scroll(1,mode='absolute')
# result4 = curser.fetchone()
# print(result4)
# curser.scroll(2)
# result5 = curser.fetchone()
# print(result5)
update_dep1 = 'update department set dep_name=%s where dep_name=%s'
curser.execute(update_dep1,('运维部开发部','运维部'))










conn.commit()
curser.close()   #游标（cursor）是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果
conn.close()