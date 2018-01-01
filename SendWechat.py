#coding=utf8
import itchat
import time
import xlrd
import datetime
import threading
# http://www.liuxue86.com/a/3151933.html

wechat = "WeChat.xlsx"

# 系统客户微信账号
admin = ['shen']

getup_hour = 7 # 起床时间
getup_min = 0 # 起床时间

sign_hour = 8 #上班时间
sign_min = 20 #上班时间

lunch_hour = 11 #午饭时间
lunch_min = 30 #午饭分钟

offwork_hour = 17 #下班小时
offwork_min = 30 #下班分钟

sign_out_hour = 17 #签退时间
sign_out_min =  36 #签退时间

extra_hour = 20 #加班时间
extra_min = 0 #加班

sleep_hour = 23 #睡觉时间
sleep_min = 0 #睡觉时间



def not_empty(s):
    return s and s.strip()

bk = xlrd.open_workbook(wechat)
try:
    sh = bk.sheet_by_index(0)
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    signInList = sh.col_values(0)
    getUpList = sh.col_values(1)
    lunchList = sh.col_values(2)
    signOutList = sh.col_values(3)
    offworkList = sh.col_values(4)
    extraworkList = sh.col_values(5)
    sleepList = sh.col_values(6)
except:
    print("no sheet in %s named Sheet1" % wechat)

getUpList.pop(0)
signInList.pop(0)
lunchList.pop(0)
signOutList.pop(0)
offworkList.pop(0)
extraworkList.pop(0)
sleepList.pop(0)
getUpList = list(filter(not_empty, getUpList))
signInList = list(filter(not_empty, signInList))
lunchList = list(filter(not_empty, lunchList))
signOutList = list(filter(not_empty, signOutList))
offworkList = list(filter(not_empty, offworkList))
extraworkList = list(filter(not_empty, extraworkList))
sleepList = list(filter(not_empty, sleepList))
print(getUpList,signInList,lunchList,signOutList,offworkList,extraworkList,sleepList)

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
        sendMsgToAdmin(msg=msg['Text'])
        # 回复给好友
        return u'[自动回复]您好，我只是段代码，有事请联系我的主人-申爷。\n您的的信息：%s  我会转达给申爷\n' % (msg['Text'])
# 起床
def notifyGetup():
    print("一天之际在于晨，起床啦")
    notifyWechat('一天之际在于晨，起床啦',getUpList)
    notifyMyself('骚年，上班啦，记得签到啊！')

# 签到
def notifySign():
    print("骚年，上班啦，记得签到啊！")
    notifyWechat("【微信提醒】骚年，上班啦，记得签到,打卡啊！",signInList)
    notifyMyself('骚年，上班啦，记得签到啊！')

# 午饭
def notifyLunch():
    print("人是铁饭是钢，午饭，走起！")
    notifyWechat("人是铁饭是钢，午饭，走起！", lunchList)
    notifyMyself('人是铁饭是钢，午饭，走起！')


# 一起下班
def notifyOffwork():
    print("一天最美的事，莫过于下班，下班，走起！")
    notifyWechat("【微信提醒】一天最美的事，莫过于下班，打卡，签退，走起！", offworkList)
    notifyMyself('一天最美的事，莫过于下班，打卡，签退，走起！')


# 签退
def notifySignOut():
    print("枯藤老树昏鸦，上班下班回家")
    notifyWechat("【微信提醒】一天最美的事，莫过于下班，但不要忘了签退", signOutList)
    notifyMyself('一天最美的事，莫过于下班，打卡，签退，走起！')

# 加班
def notifyExtraWork():
    print("加班写代码中")
    notifyWechat("【微信提醒】加吧正常，经常加班就不好了，打卡，签退，回吧！", extraworkList)
    notifyMyself('一天最美的事，莫过于下班，打卡，签退，走起！')

# 睡觉
def notifySleep():
    print("垂死病中惊坐起，今日到底星期几。抬望眼，卧槽，周一。低头，完了，十点。")
    notifyWechat('早睡早起，身体好，睡觉哇！',sleepList)

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


def notifyMyself(msg):
    # 向自己文件传输助手发消息
    itchat.send(msg, 'filehelper')


def notifyAdmin():
    notifyWechat("【提醒小能手】系统运行正常，请主人放心", admin)

def sendMsgToAdmin(msg):
    notifyWechat(msg, admin)

class myThread (threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        notifyAdmin()
        while True:

            localtime = time.localtime(time.time())
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

            dayOfWeek = datetime.datetime.now().weekday()
            print("今天是星期", dayOfWeek + 1)

            s_hour = localtime.tm_hour
            s_min = localtime.tm_min

            print("现在时间：", s_hour, ":", s_min)

            #s_hour = int(input("请输入小时："))
            #s_min = int(input("请输入分钟："))

            # 每半小时通知一次
            if (s_min == 30 or s_min == 0):
                notifyAdmin()

            if dayOfWeek == 5 or dayOfWeek == 6:
                print("今天是周末")
                time.sleep(60 * 20)
            # 进行提示
            elif getup_hour == s_hour and getup_min == s_min:
                notifyGetup()
            elif sign_hour == s_hour and sign_min == s_min:
                notifySign()
            elif lunch_hour == s_hour and lunch_min == s_min:
                notifyLunch()
            elif offwork_hour == s_hour and offwork_min == s_min:
                notifyOffwork()
            elif sign_out_hour == s_hour and sign_out_min == s_min:
                notifySignOut()
            elif extra_hour == s_hour and extra_min == s_min:
                notifyExtraWork()
            elif sleep_hour == s_hour and sleep_min == s_min:
                notifySleep()
            if s_hour < (getup_hour - 1) or s_hour > (sleep_hour + 1):
                time.sleep(60 * 20)
            else:
                time.sleep(60)



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
    try:
        thread1 = myThread(1, "Thread-1")
        thread1.start()
    except:
        print("Error: 无法启动线程")

    itchat.run()

    #tchat.send(u"系统退出运行", 'filehelper')
