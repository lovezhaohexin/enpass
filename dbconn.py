#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Date,ForeignKey

#创建链接数据库的引擎

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/tedu1809?charset=utf8',
    #用户名:密码@服务器/数据库?字符集
    encoding = 'utf8', #指定字符集
    echo = True        #控制台显示详细日志输出,生产环境下关闭
)

Session = sessionmaker(bind=engine)




#创建ORM映射的基类   部门表
Base = declarative_base()
#
class Departments(Base):
    #继承于基类Base,对应数据库中的一张表

    __tablename__ = 'departments'    #声明该类对应哪张表
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True,nullable=False)

    def __src__(self):
        return "部门: %s" % self.dep_name


#员工表
class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20),nullable=False)
    gender = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))

    def __str__(self):
        return "员工: %s" % self.emp_name


#工资表
class Salary(Base):
    __tablename__ = 'salary'

    auto_id =Column(Integer,primary_key=True)
    emp_id = Column(Integer,ForeignKey('employees.emp_id'))
    awards = Column(Integer)
    basic = Column(Integer)
    data = Column(Date)







if __name__ == '__main__':
    Base.metadata.create_all(engine)


