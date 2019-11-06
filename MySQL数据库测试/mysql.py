# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "username", "password", "dbname", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

create = "create table test(\
	id int not null auto_increment,\
    name varchar(8),\
    birthday datetime,\
    constraint pk__person primary key(id));"

insert = "insert into test(id,name,birthday) values(1,'zhang','1992-12-01'),(2,'wang','1992-12-01');"

select = "select * from test;"

delete = "delete from test where id=2"

update = "update test set name='liu' where name='wang'"

drop = "drop table test"

try:
	# 使用execute方法执行SQL语句
	cursor.execute(drop)
	db.commit()
except:
	db.rollback()

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
# data = cursor.fetchall()

print data

# 关闭数据库连接
db.close()