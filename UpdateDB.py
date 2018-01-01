#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "cqtddt@2016", "joke")
db.set_charset('utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 打开数据库
def open_db():
    global db, cursor
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "cqtddt@2016", "joke")
    db.set_charset('utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()


def create_mysql_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS JOKEHISTORY")

    # 使用预处理语句创建表
    sql = """CREATE TABLE JOKEHISTORY (HISTORY_ID BIGINT primary key AUTO_INCREMENT  NOT NULL ,HISTORY_NET_SITE  CHAR(150),HISTORY_DATE CHAR(20)) DEFAULT CHARSET=utf8"""

    try:
        cursor.execute(sql)
        print("创建表成功")
    except:
        db.rollback()
        print("创建表失败")


def close_joke_db():
    cursor.close()
    db.close


def insert_mysql_data(site):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # SQL 插入语句
    sql = """INSERT INTO JOKEHISTORY(HISTORY_NET_SITE,HISTORY_DATE) VALUES ('%s', '%s') """
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


def query_mysql_data():
    result = ''
    # SQL 查询语句
    sql = "SELECT * FROM JOKEHISTORY ORDER BY HISTORY_ID DESC"
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


def is_exit_table():
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '%s'"
    # 执行SQL语句
    cursor.execute(sql % 'JOKEHISTORY')
    # 获取所有记录列表
    results = cursor.fetchall()
    if 'JOKEHISTORY' in results:
        print("已经存在数据表")
    else:
        print("不存在数据表")


if __name__ == '__main__':
    create_mysql_table()
    # insert_mysql_data("www.baidu.com","百度一下，就知道")
    # joke = query_mysql_data()
    # joke_json = json.dumps(joke,ensure_ascii=False)
    # print(joke_json)
    # close_joke_db()
    # insert_mysql_data('/jokehtml/冷笑话/201709082323108.htm')
    # is_exit_table()
