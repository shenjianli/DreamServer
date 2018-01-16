# coding=utf8

import itchat
import time
import DreamDB
import datetime
import threading
import Config


def not_empty(s):
    return s and s.strip()


# 系统默认服务提示语
server_hint = u'[梦想号]您好，您的梦想信息我已经收到, 稍后小梦将为你服务'


# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:

        # 发送一条提示给文件助手
        # itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
        #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        #                  msg['User']['NickName'],
        #                  msg['Text']), 'filehelper')

        print("昵称：", msg['User']['NickName'])
        print("内容：", msg['Text'])

        we_chat_msg_content = msg['Text']

        if '_' in we_chat_msg_content:

            msg_content = we_chat_msg_content.split('_')
            print(msg_content)

            if len(msg_content) >= 2:
                op = str(msg_content[0])
                # 放飞梦想
                if op == 'A' or op == 'a':
                    return add_dream(msg, msg_content)
                # 删除梦想
                elif op == 'D' or op == 'd':
                    if len(msg_content) >= 2:
                        result = DreamDB.delete_dream_by_id(msg_content[1])
                        if result != '' and result != '0':
                            return u'[梦想号] 您的梦想已经化为泡影！'
                        elif result == '0':
                            return u'[梦想号] 请确保你的梦想ID正确'
                        else:
                            return server_hint
                    else:
                        return u'[梦想号] 删除梦想参数有误'
                # 修改梦想
                elif op == 'M' or op == 'm':
                    if len(msg_content) >= 4:
                        result = DreamDB.update_dream_by_id(msg_content[1], msg_content[2], msg_content[3])
                        if result != '':
                            return u'[梦想号] 恭喜您，您的梦想信息修改成功！'
                        else:
                            return server_hint
                    else:
                        return u'[梦想号] 修改梦想参数有误'
                # 查询梦想
                elif op == 'Q' or op == 'q':

                    if len(msg_content) >= 2:
                        query_result = DreamDB.query_dream_by_id(msg_content[1])
                        if len(query_result) != 0:
                            dream_item = query_result[0]
                            print("查询到梦想数据为", dream_item[1], dream_item[2])
                            return u'[梦想号] 恭喜您，您的梦想信息为：\n名称：%s\n内容：%s' % (dream_item[1], dream_item[2])
                        else:
                            return server_hint
                    else:
                        return u'[梦想号] 查询梦想参数有误'
                # 完成梦想
                elif op == 'F' or op == 'f':
                    if len(msg_content) >= 2:
                        result = DreamDB.finish_dream_by_id(msg_content[1])
                        if result != '':
                            return u'[梦想号] 您真历害，恭喜您，实现了自己梦想！'
                        else:
                            return server_hint
                    else:
                        return u'[梦想号] 完成梦想参数有误'
        else:
            return u'[梦想号]您好，欢迎进入梦想号，请按下面指令驾驭您的梦想：\n' \
                   u'(1)放飞梦想（A_梦想名称_梦想内容）\n' \
                   u'(2)修改梦想（M_梦想ID_梦想名_梦想内容）\n' \
                   u'(3)查询梦想（Q_梦想ID）\n' \
                   u'(4)删除梦想（D_梦想ID）\n' \
                   u'(5)实现梦想（F_梦想ID）\n' \
                   u'非常感谢您搭乘梦想号！'
        # 回复给好友
        return server_hint


def add_dream(msg, msg_content):
    if len(msg_content) >= 3:
        dream_name = msg_content[1]
        dream_content = msg_content[2]
        if len(dream_name) < 2:
            return u'梦想名过短'
        if len(dream_content) < 10:
            return u'梦想内容过短'
        dream_id = DreamDB.insert_dream_data(dream_name, dream_content, msg['User']['NickName'], '')
        if dream_id != '':
            print("梦想名称：", dream_name)
            print("梦想内容：", dream_content)
            return u"[梦想号] 恭喜您，您的梦想放飞成功！\n 您的梦想ID为：%s" % dream_id
        else:
            return server_hint
    else:
        return u'[梦想号] 放飞梦想参数有误'


# 向微信发送消息
def notify_wechat_by_nick_name(msg, nick):
    print(msg, nick)
    if nick == "" or nick is None:
        print("名字为空不进行发送")
    else:
        print('发消息给：' + nick)
        # 想给谁发信息，先查找到这个朋友
        users = itchat.search_friends(name=nick)
        # 找到UserName
        userName = users[0]['UserName']
        # 然后给他发消息
        itchat.send(msg, toUserName=userName)


# 向微信发送消息
def notifyWechat(msg, person):
    print(msg, person)
    for p in person:
        if p == "":
            print("名字为空不进行发送")
        else:
            # 想给谁发信息，先查找到这个朋友
            users = itchat.search_friends(name=p)
            # 找到UserName
            userName = users[0]['UserName']
            # 然后给他发消息
            itchat.send(msg, toUserName=userName)


# 通知系统管理员系统运行情况
def notify_admin(msg):
    # 向自己文件传输助手发消息
    itchat.send(msg, 'filehelper')


# 构想提示线程
class DreamNoitfyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            localtime = time.localtime(time.time())
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

            dayOfWeek = datetime.datetime.now().weekday()
            print("今天是星期", dayOfWeek + 1)

            s_hour = localtime.tm_hour
            s_min = localtime.tm_min

            print("现在时间：", s_hour, ":", s_min)

            # s_hour = int(input("请输入小时："))
            # s_min = int(input("请输入分钟："))

            # 每半小时通知一次
            if s_min == 30 or s_min == 0:
                notify_admin('系统运行正常')
            # 如果测试模式5分钟提示一次
            if Config.isDebug:
                # 通知梦想号所有梦想，大约每5分钟提示一次
                if s_min % 5 == 0:

                    dream_data = DreamDB.query_dream_data_by_id()

                    for row in dream_data:
                        id = row[0]
                        name = row[1]
                        content = row[2]
                        nick = row[3]
                        date = row[4]
                        finish = row[5]

                        if finish == '' or finish is None:
                            print(id, name, content, nick, date)
                            hint_msg = '[梦想号] 您于 ' + date + " 放飞的梦想：\n\"" + content + "\"\n呼唤您----" + "为实现它努力，加油！"
                            # hint_msg = '[梦想号] 您于' + date + "放飞的梦想：" + content + "呼唤您----" + "实现不梦想，不止是三分钟热度"
                            notify_wechat_by_nick_name(hint_msg, nick)
            # 如果非测试模式每天只提示一次
            else:
                if s_min == Config.dream_hint_min and s_hour == Config.dream_hint_hour:
                    dream_data = DreamDB.query_dream_data_by_id()

                    for row in dream_data:
                        id = row[0]
                        name = row[1]
                        content = row[2]
                        nick = row[3]
                        date = row[4]
                        finish = row[5]

                        if finish == '':
                            print(id, name, content, nick, date)
                            hint_msg = '[梦想号] 您于 ' + date + " 放飞的梦想：\n\"" + content + "\"\n呼唤您----" + "为实现它努力，加油！"
                            # hint_msg = '[梦想号] 您于' + date + "放飞的梦想：" + content + "呼唤您----" + "实现不梦想，不止是三分钟热度"
                            notify_wechat_by_nick_name(hint_msg, nick)

            time.sleep(60)


# 开启梦想号的主方法
if __name__ == '__main__':

    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    # 向自己文件传输助手发消息
    notify_admin("系统开始运行")

    # 创建线程
    try:
        dream_thread = DreamNoitfyThread(1988, "Thread-Dream")
        dream_thread.start()
    except:
        print("Error: 无法启动线程")

    itchat.run()
