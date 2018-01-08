#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time

import pymysql
import json

import Config

# 打开数据库连接
db = pymysql.connect(Config.mysql_net_site, Config.mysql_user, Config.mysql_pass, Config.mysql_db)
db.set_charset('utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 打开数据库
def open_db():
    global db, cursor
    # 打开数据库连接
    db = pymysql.connect(Config.mysql_net_site, Config.mysql_user, Config.mysql_pass, Config.mysql_db)
    db.set_charset('utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()


# 创建梦想加油文字数据库表
def create_dream_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("drop table if exists comment")

    # 使用预处理语句创建表
    sql = """create table comment(comment_id BIGINT primary key AUTO_INCREMENT NOT NULL, dream_id BIGINT, 
    comment_content TEXT, comment_date CHAR(20)) DEFAULT CHARSET = utf8 """

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
def insert_comment_data(dream_id, comment_content):

    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # SQL 插入语句
    sql = """insert into comment(dream_id,comment_content ,comment_date) VALUES ('%s', '%s', '%s') """
    try:
        # 执行sql语句
        cursor.execute(sql % (dream_id, comment_content, datetime))
        # 提交到数据库执行
        db.commit()
        print("[梦想号] ", comment_content,  " 梦想加油数据插入成功")
        return '1'
    except Exception:
        # 如果发生错误则回滚
        db.rinsert_dream_dataollback()
        print("[梦想号] 梦想加油数据插入失败")
        return ''
    return ''


# 查询梦想加油数据，返回json字符串
def query_comment_data(dream_id):
    list = []
    item = {}
    # SQL 查询语句
    sql = "select * from comment where dream_id = '%s'"
    try:
        # 执行SQL语句
        cursor.execute(sql % dream_id)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            list.append(row[2])
            # 打印结果
            print("id=%d,comment=%s" % (dream_id, row[2]))

        item['code'] = 1
        item['msg'] = '查询成功'
        item['data'] = list
    except:
        print("Error: unable to fetch data")
    return item


# 主方法
if __name__ == '__main__':

    # 创建梦想号使用的数据表
    # create_dream_table()
    #
    # insert_comment_data(1, "不错，不错，梦想的味道真不错")
    # insert_comment_data(1, "加油向未来")

    #
    joke = query_comment_data(1)
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)

    #delete_dream_by_id(1)

    # update_dream_by_id(2, "111111", "222222222")

    # result = query_dream_data_by_id()
    # if len(result) != 0:
    #     for row in result:
    #         print(row[0], row[1], row[2], row[3])
    #         if row[5] == '':
    #             print("空")
    #         else:
    #             print(row[5])

    #close_joke_db()
