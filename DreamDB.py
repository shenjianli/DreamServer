#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import pymysql
import json
import IDGenerator

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


# 查看mysql版本号
def select_mysql_version():
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select version()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)
    # 关闭数据库连接
    return data


# 创建梦想数据库表
def create_dream_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("drop table if exists dream")

    # 使用预处理语句创建表
    sql = """create table dream(dream_id BIGINT primary key AUTO_INCREMENT NOT NULL, dream_name CHAR(150), dream_content TEXT, we_chat_name char(50), dream_date CHAR(20), dream_finish_date CHAR(20),dream_uuid char(20)) DEFAULT CHARSET = utf8 """

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


# 向数据库中插入数据
def insert_dream_data(dream_name, dream_content, we_chat_name):

    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dream_uuid = IDGenerator.get_dream_id();
    dream_finish_date = ''
    # SQL 插入语句
    sql = """insert into dream(dream_name,dream_content,we_chat_name ,dream_date,dream_finish_date,dream_uuid) VALUES ('%s', '%s', '%s', '%s','%s', '%s') """
    try:
        # 执行sql语句
        result = cursor.execute(sql % (dream_name, dream_content, we_chat_name, datetime, dream_finish_date, dream_uuid))
        # 提交到数据库执行
        db.commit()
        print("[梦想号]-", dream_content,  "-梦想插入成功")
        print(result)
    except Exception:
        # 如果发生错误则回滚
        db.rinsert_dream_dataollback()
        print("fail")
        return ''
    return dream_uuid


# 根据 id 删除指定梦想
def delete_dream_by_id(dream_id):
    # SQL 查询语句
    # 删除记录
    sql = "delete from dream where dream_uuid = '%s'"

    try:
        # 执行SQL语句
        cursor.execute(sql % dream_id)
        db.commit()
        print("[梦想号]", dream_id, "删除成功")
    except:
        db.rollback()
        print("Error: unable to fetch data")


# 根据 id 完成指定梦想
def finish_dream_by_id(dream_id):

    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sql = "update dream set dream_finish_date = '%s' where dream_uuid = '%s'"

    try:
        # 执行SQL语句
        cursor.execute(sql % (datetime, dream_id))
        db.commit()
        print("[梦想号]", dream_id, "梦想完成成功")
    except:
        db.rollback()
        print("Error: unable to fetch data")


# 根据 id 更新指定梦想
def update_dream_by_id(dream_id, dream_name, dream_content):
    # SQL 查询语句
    # 删除记录
    sql = "update dream set dream_name = '%s', dream_content = '%s' where dream_uuid = '%s'"

    try:
        # 执行SQL语句
        cursor.execute(sql % (dream_name, dream_content, dream_id))
        db.commit()
        print("[梦想号]", dream_id, "修改成功")
    except:
        db.rollback()
        print("Error: unable to fetch data")


# 根据梦想号查询梦想数据，返回json字符串
def query_dream_by_id(dream_id):
    # SQL 查询语句
    sql = "select * from dream where dream_uuid = '%s'"
    try:
        # 执行SQL语句
        cursor.execute(sql % dream_id)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    return results


# 查询梦想数据，返回json字符串
def query_dream_data():
    list = []
    item = {}
    # SQL 查询语句
    sql = "select * from dream"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            data = {}

            id = row[0]
            data['id'] = id

            name = row[1]
            data['name'] = name

            content = row[2]
            data['content'] = content

            nick = row[3]
            data['nick'] = nick

            date = row[4]
            data['date'] = date

            list.append(data)
            # 打印结果
            print("id=%d,name=%s,content=%s,nick=%s,date=%s" % (id, name, content, nick, date))

        item['code'] = 1
        item['msg'] = '查询成功'
        item['data'] = list
        item['dreams'] = list
    except:
        print("Error: unable to fetch data")
    return item


# 查询梦想数据
def query_dream_data_by_id():
    sql = "select * from dream order BY dream_id * 1 asc"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("Error: unable to fetch data")
    # joke_item['jokes'] = joke_list
    return results


# 查询梦想数据个数
def query_joke_data_count():
    # SQL 查询语句
    sql = "select count(*) from dream"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        count = int(result[0][0])
    except:
        print("Error: unable to fetch data")
    # joke_item['jokes'] = joke_list
    return count


# 主方法
if __name__ == '__main__':
    version = select_mysql_version()

    print("Database mysql : %s " % version)

    create_dream_table()

    insert_dream_data("2018找个好老婆", "希望自己在2018年，可以找个好老婆", "Jerry")
    #
    # joke = query_dream_data()
    # joke_json = json.dumps(joke, ensure_ascii=False)
    # print(joke_json)

    #delete_dream_by_id(1)

    # update_dream_by_id(2, "111111", "222222222")

    result = query_dream_data_by_id()
    if len(result) != 0:
        for row in result:
            print(row[0], row[1], row[2], row[3])
            if row[5] == '':
                print("空")
            else:
                print(row[5])

    close_joke_db()
