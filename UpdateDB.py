#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "cqtddt@2016", "dream")
db.set_charset('utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 打开数据库
def open_db():
    global db, cursor
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "cqtddt@2016", "dream")
    db.set_charset('utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

# 创建更新历史记录表
def create_history_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("drop table if exists jokehistory")

    # 使用预处理语句创建表
    sql = """create table jokehistory (history_id BIGINT primary key AUTO_INCREMENT  NOT NULL ,history_net_site  CHAR(150),history_date CHAR(20)) DEFAULT CHARSET=utf8"""

    try:
        cursor.execute(sql)
        print("创建表成功")
    except:
        db.rollback()
        print("创建表失败")


# 关闭数据库
def close_joke_db():
    cursor.close()
    db.close


# 插入更新的历史记录
def insert_history_data(site):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # SQL 插入语句
    sql = """insert into jokehistory(history_net_site,history_date) VALUES ('%s', '%s') """
    try:
        # 执行sql语句
        cursor.execute(sql % (site, datetime))
        # 提交到数据库执行
        db.commit()
        print("success")
    except Exception:
        # 如果发生错误则回滚
        db.rollback()
        print("fail")


# 查看历史记录
def query_history_data():
    result = ''
    # SQL 查询语句
    sql = "select * from jokehistory order by history_id desc"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) != 0:
            history = results[0]
            if len(history) != 0:
                result = history[1]
    except:
        print("Error: unable to fetch data")
    return result


# 判断是否存在表结构
def is_exit_table():
    sql = "select * from information_schema.tables where table_name = '%s'"
    # 执行SQL语句
    cursor.execute(sql % 'jokehistory')
    # 获取所有记录列表
    results = cursor.fetchall()
    if 'jokehistory' in results:
        print("已经存在数据表")
    else:
        print("不存在数据表")


if __name__ == '__main__':
    create_mysql_table()
