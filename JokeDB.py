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


# 查看mysql版本号
def select_mysql_version():
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select version()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)
    # 关闭数据库连接
    return data


# 创建Joke表
def create_joke_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("drop table if exists joke")

    # 使用预处理语句创建表
    sql = """create table joke(joke_id BIGINT primary key AUTO_INCREMENT NOT NULL, joke_net_site CHAR(150), joke_content TEXT, joke_date CHAR(20) ) DEFAULT CHARSET = utf8 """

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


# 向数据库中插入
def insert_mysql_data(site, content):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # SQL 插入语句
    sql = """insert into joke(joke_net_site,joke_content, joke_date) VALUES ('%s', '%s', '%s') """
    try:
        # 执行sql语句
        cursor.execute(sql % (site, content, datetime))
        # 提交到数据库执行
        db.commit()
        print("success")
    except Exception:
        # 如果发生错误则回滚
        db.rollback()
        print("fail")
    # 关闭数据库连接


# 查询笑话数据，返回json字符串
def query_mysql_data():
    joke_list = []
    joke_item = {}
    # SQL 查询语句
    sql = "select * from joke"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            joke_data = {}
            joke_id = row[0]
            joke_data['id'] = joke_id
            joke_site = row[1]
            joke_data['site'] = joke_site
            joke_content = row[2]
            if '<BR>' in joke_content:
                joke_content = joke_content.replace("<BR>", "\n")
            joke_data['content'] = joke_content
            joke_date = row[3]
            joke_data['date'] = joke_date
            joke_list.append(joke_data)
            # 打印结果
            print("id=%d,site=%s,content=%s,date=%s" % (joke_id, joke_site, joke_content, joke_date))
        joke_item['code'] = 1
        joke_item['msg'] = '查询成功'
        joke_item['data'] = joke_list;
        joke_item['jokes'] = joke_list
    except:
        print("Error: unable to fetch data")
    return joke_item


# 查询笑话数据，返回json字符串
def query_mysql_data_by_num(num):
    joke_list = []
    joke_item = {}
    # SQL 查询语句
    sql = "select * from joke ORDER BY joke_id * 1 DESC  limit %d"
    try:
        # 执行SQL语句
        cursor.execute(sql % num)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            joke_data = {}
            joke_id = row[0]
            joke_data['id'] = joke_id
            joke_site = row[1]
            joke_data['site'] = joke_site
            joke_content = row[2]
            if '<BR>' in joke_content:
                joke_content = joke_content.replace("<BR>", "\n")
            joke_data['content'] = joke_content
            joke_date = row[3]
            joke_data['date'] = joke_date
            joke_list.append(joke_data)
            # 打印结果
            print("id=%d,site=%s,content=%s,date=%s" % (joke_id, joke_site, joke_content, joke_date))
        joke_item['code'] = 1
        joke_item['msg'] = '查询成功'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    except:
        print("Error: unable to fetch data")
        joke_item['code'] = -1
        joke_item['msg'] = '服务器异常'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    return joke_item


# 查询笑话数据，返回json字符串
def query_mysql_data_by_date(date):
    joke_list = []
    joke_item = {}
    # SQL 查询语句
    sql = "select * from joke where joke_date > '%s'"
    try:
        # 执行SQL语句
        cursor.execute(sql % date)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            joke_data = {}
            joke_id = row[0]
            joke_data['id'] = joke_id
            joke_site = row[1]
            joke_data['site'] = joke_site
            joke_content = row[2]
            if '<BR>' in joke_content:
                joke_content = joke_content.replace("<BR>", "\n")
            joke_data['content'] = joke_content
            joke_date = row[3]
            joke_data['date'] = joke_date
            joke_list.append(joke_data)
            # 打印结果
            print("id=%d,site=%s,content=%s,date=%s" % (joke_id, joke_site, joke_content, joke_date))
        joke_item['code'] = 1
        joke_item['msg'] = '查询成功'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    except:
        print("Error: unable to fetch data")
        joke_item['code'] = -1
        joke_item['msg'] = '服务器异常'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    return joke_item


# 查询笑话数据，返回json字符串
def query_joke_data_by_id(end):
    joke_list = []
    joke_item = {}
    # SQL 查询语句
    sql = "select * from joke where joke_id > %d"
    try:
        # 执行SQL语句
        cursor.execute(sql % end)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            joke_data = {}
            joke_id = row[0]
            joke_data['id'] = joke_id
            joke_site = row[1]
            joke_data['site'] = joke_site
            joke_content = row[2]
            if '<BR>' in joke_content:
                joke_content = joke_content.replace("<BR>", "\n")
            joke_data['content'] = joke_content
            joke_date = row[3]
            joke_data['date'] = joke_date
            joke_list.append(joke_data)
            # 打印结果
            print("id=%d,site=%s,content=%s,date=%s" % (joke_id, joke_site, joke_content, joke_date))
        joke_item['code'] = 1
        joke_item['msg'] = '查询成功'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    except:
        print("Error: unable to fetch data")
        joke_item['code'] = -1
        joke_item['msg'] = '服务器异常'
        joke_item['data'] = joke_list;
    # joke_item['jokes'] = joke_list
    return joke_item


# 查询笑话数据，返回json字符串
def query_joke_data_count():
    # SQL 查询语句
    sql = "select count(*) from joke"
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

    create_joke_table()

    # insert_mysql_data("http://www.i2finance.net/pc/index.html","艾融软件")
    # joke = query_mysql_data()
    # joke_json = json.dumps(joke,ensure_ascii=False)
    # print(joke_json)
    # close_joke_db()
