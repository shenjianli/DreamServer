#!/usr/bin/python3
import DreamDB
import DreamWechat




if __name__ == '__main__':
    dream_data = DreamDB.query_dream_data_by_id()
    for row in dream_data:
        id = row[0]
        name = row[1]
        content = row[2]
        nick = row[3]
        date = row[4]
        print(id, name,content,nick,date)
        hint_msg = '[梦想号] 您于' + date + "放飞的梦想：" + content + "呼唤您----" + "为实现梦想加油，努力！"
        #hint_msg = '[梦想号] 您于' + date + "放飞的梦想：" + content + "呼唤您----" + "实现不梦想，不止是三分钟热度"
        DreamWechat.notify_wechat_by_nick_name(hint_msg,'shen')