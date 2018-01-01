#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import pymysql
import json

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


# 创建对联couplet表
def create_mysql_table():
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("drop table if exists couplet")

    # 使用预处理语句创建表
    sql = """create table couplet(couplet_id BIGINT primary key AUTO_INCREMENT NOT NULL, couplet_title CHAR(150), couplet_left TEXT, couplet_right TEXT, couplet_date CHAR(20) ) DEFAULT CHARSET = utf8 """

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


# 向对联数据库中插入数据
def insert_couplet_data(title, left, right):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # SQL 插入语句
    sql = """insert into couplet(couplet_title,couplet_left,couplet_right ,couplet_date) VALUES ('%s', '%s', '%s', '%s') """
    try:
        # 执行sql语句
        cursor.execute(sql % (title, left, right, datetime))
        # 提交到数据库执行
        db.commit()
        print("[梦想号]-", title, "-梦想对联插入成功")
    except Exception:
        # 如果发生错误则回滚
        db.rinsert_dream_dataollback()
        print("fail")
        # 关闭数据库连接


# 查询对联数据，返回json字符串
def query_couplet_data():
    list = []
    item = {}
    # SQL 查询语句
    sql = "select * from couplet"
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
            data['title'] = name

            content = row[2]
            data['left'] = content

            nick = row[3]
            data['right'] = nick

            date = row[4]
            data['date'] = date

            list.append(data)
            # 打印结果
            print("id=%d,title=%s,left=%s,right=%s,date=%s" % (id, name, content, nick, date))

        item['code'] = 1
        item['msg'] = '查询成功'
        item['data'] = list
    except:
        print("Error: unable to fetch data")
    return item


# 查询数据库中的对联数目
def query_joke_data_count():
    # SQL 查询语句
    sql = "select count(*) from couplet"
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

    # 创建数据表
    create_mysql_table()

    # 插入对联数据
    insert_couplet_data("志在四方", "雄心状志要我将来", "脚踏实地看我今朝")
    insert_couplet_data("奋斗一生", "寻几许阳光放飞梦想", "驾一叶扁舟挥洒青春")
    insert_couplet_data("我最牛逼", "足不出户一台电脑打天下", "宅男在家两只巧手定乾坤")
    insert_couplet_data("细思恐极", "我这儿没干啥它自己就好了", "你那儿不行吗我运行正常呀")
    insert_couplet_data("鞠躬尽瘁", "文档注释一应俱全", "脊柱腰椎早日康复")
    insert_couplet_data("一代键客", "坐北朝南一个需求满足东西", "思前想后几行代码安抚中央")
    insert_couplet_data("运鼠帷幄", "读码上万行", "下键如有神")
    insert_couplet_data("画饼充饥", "百个功能愿你一气呵成", "明年年终奖你十月工资")
    insert_couplet_data("瞬息万变", "微博知乎占头条谁与争锋", "桌面移动待前端一统江湖")
    insert_couplet_data("生不如死", "一年三百六十五天天天打代码", "十兆九千八百七行行行见bug")
    insert_couplet_data("风调码顺", "上拜图灵只佑服务可用", "下跪关公但求永不宕机")
    insert_couplet_data("码到成功", "废寝忘食编程序", "闻机起早保运维")

    joke = query_couplet_data()

    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)

    # 关闭数据库
    close_joke_db()
