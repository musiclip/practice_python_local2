import pymysql
import pandas as pd
from sqlalchemy import create_engine

#mydb = pymysql.connect(host = 'localhost', user = 'root', password = 'zxc098')
#mydb = pymysql.connect(host = 'localhost', user = 'pmth', db = 'testdb')
mydb = pymysql.connect(host = 'localhost', user = 'pmth', db = 'mydatabase')

mycursor = mydb.cursor()

#pmth testdb 계정 사용
def print_result(sql, cur = mycursor):
    cur.execute(sql)
    result = mycursor.fetchall()
    if result:
        for i in result:
            print(i)
        print('=='*10)

def show_query():
    sql = "show databases;"
    print_result(sql)

    sql = "use keos;"
    print_result(sql)

    sql = "show tables;"
    print_result(sql)

#루트계정 사용
def create_db():
    sql = "create database mydatabase"
    print_result(sql)

    sql = "show databases;"
    print_result(sql)

#mydatabase 계정 사용
def create_tables():
    sql = "create table members (name VARCHAR(255), address VARCHAR(255));"
    print_result(sql)

    sql = "show tables;"
    print_result(sql)

def desc_query():
    sql = "desc members"
    print_result(sql)

def insert_data():
    sql = "insert into members values('Tom', 'Highway 28');"
    print_result(sql)
    sql = "select * from members"
    print_result(sql)
#커밋을 하지 않아 데이터가 들어갔다가 사라짐
# 데이터 올릴땐 커밋 꼭 하기! 데이터베이스나 테이블을 만들땐 커밋을 안해도 됨

def insert_member(cur = mycursor):
    sql = "insert into members (name, address) values (%s, %s);"
    val = ("Tom", "Highway 28")
    cur.execute(sql, val)
    print(mycursor.rowcount, " record inserted.")

    mydb.commit()

    sql = "select * from members"
    print_result(sql)

def insert_manydata():
    sql = "select * from members"
    print_result(sql)
    sql = "insert into members (name, address) values (%s, %s);"
    val = [
            ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633')
            ]
    mycursor.executemany(sql, val)
    mydb.commit()

    print(mycursor.rowcount, " record inserted.")
    print("id : ", mycursor.lastrowid)
    sql = "select * from members"
    print_result(sql)

def select_():
    sql = "select * from members where address like %s"
    val = ("%way%")
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    for x in result:
        print(x)
    return result

def delete_commit():
    sql = "delete from members where address = 'Highway 28';"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount)
    print_result('select * from members;')

def order_by():
    sql = "select * from members order by name desc;"
    print_result(sql)

def update_data():
    sql = "select * from members where address = %s;"
    val = ("Valley 345")
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    for x in result:
        print(x)

    sql = "update members set address = %s where address = %s;"
    val = ("Canyon 123", "Valley 345")
    mycursor.execute(sql,val)
    mydb.commit()

    sql = "select * from members;"
    print_result(sql)

def limit_offset():
    sql = "select * from members limit 5 offset 2;"
    print_result(sql)

def close_conx():
    mydb.close()

def join_():
    sql = "select users.name, products.name from users \
        join products on users.fav = products.id;"
    print_result(sql)