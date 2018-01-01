#coding=utf8
import itchat
import time

import datetime
import threading

def not_empty(s):
    return s and s.strip()

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        print("昵称：", msg['User']['NickName'])
        print("内容：", msg['Text'])
        # 回复给好友
        return u'[梦想号]您好，您的梦想信息我已经收到'


# 向微信发送消息
def notifyWechat(msg,person):
    print(msg,person)
    for p in person:
        if p == "":
            print("名字为空不进行发送")
        else:
            # 想给谁发信息，先查找到这个朋友
            users = itchat.search_friends(name= p)
            # 找到UserName
            userName = users[0]['UserName']
            # 然后给他发消息
            itchat.send(msg, toUserName=userName)


class myThread (threading.Thread):

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


if __name__ == '__main__':


    ''''
    
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    # 向自己文件传输助手发消息
    itchat.send(u"开始", 'filehelper')


    # 想给谁发信息，先查找到这个朋友
    users = itchat.search_friends(name=u'吴佳健')
    # 找到UserName
    userName = users[0]['UserName']
    # 然后给他发消息
    itchat.send('hello', toUserName=userName)

    #user = itchat.search_friends(name=u'吴佳健')[0]
    #user.send(u'机器人say hello')

    # 想给谁发信息，先查找到这个朋友
    users = itchat.search_friends()
    # 找到UserName
    userName = users[0]['UserName']
    # 然后给他发消息
    itchat.send('hello', toUserName=userName)

    itchat.run()'''


    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    # 向自己文件传输助手发消息
    itchat.send(u"系统开始运行", 'filehelper')
    print("系统开始运行")

    # 创建线程
    # try:
    #     thread1 = myThread(1, "Thread-1")
    #     thread1.start()
    # except:
    #     print("Error: 无法启动线程")

    itchat.run()

    #tchat.send(u"系统退出运行", 'filehelper')
