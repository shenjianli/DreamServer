# DreamServer

## 命令使用
### 1.放飞梦想
A_梦想名_梦想内容
### 2.删除梦想
D_梦想ID
### 3.修改梦想
M_梦想ID_梦想名_梦想内容
### 4.查询梦想
Q_梦想ID
### 5.实现梦想
F_梦想ID

## 运行
### 1.安装mysql数据库
安装mysql具体方法，请自行安装
### 2.配置mysql数据库
#### 2.1 创建数据库
使用命令
```
create database dream;
```
#### 2.2 配置数据库
打开Config.py文件内容如下

```
# 梦想号相关配置

# 表示是否为测试模式
isDebug = True

# mysql地址
mysql_net_site = 'localhost'
# mysql用户名
mysql_user = 'root'
# mysql密码
mysql_pass = 'cqtddt@2016'
# mysql数据库名
mysql_db = 'dream'


# 服务器端口
dream_server_port = 8085
# 服务器地址
dream_server_site = '0.0.0.0'

# 表示梦想号每天提示时间点
dream_hint_hour = 8
dream_hint_min = 30
```
进行对应的配置即可

#### 2.3 创建数据表
可以使用命令
```
python DreamDB.py
```
来生成数据表

### 运行梦想号
使用命令
```
python DreamMain.py

```
过一会会弹出一张二维码，用微信进行扫描登录后，出现下面信息：
```
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
TERM environment variable not set.
Login successfully as Jerry
Start auto replying.
```
这就表示梦想号已经起飞成功

## 服务器
### 1.启动服务
通过命令
```
python DreamServer.py
```
来启动服务提供通过url来文访问json字符串
### 2.使用服务

浏览器中输入  http://0.0.0.0:8085/dream/query
返回json字符串：
```
{"code": 1, "msg": "查询成功", "data":
[{"id": 1, "name": "2018找个好老婆", "content": "希望自己在2018年，可以找个好老婆", "nick": "Jerry", "date": "2018-01-02 10:11:38"},
{"id": 2, "name": "1111222", "content": "8888888", "nick": "Jerry", "date": "2018-01-02 10:27:13"},
{"id": 4, "name": "找个好老婆", "content": "希望自己可以在2018年找到一个好老婆", "nick": "JerryShen", "date": "2018-01-02 13:40:33"}]}
```

## 数据表结构
对联表（couplet）结构：
```
+---------------+------------+------+-----+---------+----------------+
| Field         | Type       | Null | Key | Default | Extra          |
+---------------+------------+------+-----+---------+----------------+
| couplet_id    | bigint(20) | NO   | PRI | NULL    | auto_increment |
| couplet_title | char(150)  | YES  |     | NULL    |                |
| couplet_left  | text       | YES  |     | NULL    |                |
| couplet_right | text       | YES  |     | NULL    |                |
| couplet_date  | char(20)   | YES  |     | NULL    |                |
+---------------+------------+------+-----+---------+----------------+
```
梦想表（dream）结构：
```
+-------------------+------------+------+-----+---------+----------------+
| Field             | Type       | Null | Key | Default | Extra          |
+-------------------+------------+------+-----+---------+----------------+
| dream_id          | bigint(20) | NO   | PRI | NULL    | auto_increment |
| dream_name        | char(150)  | YES  |     | NULL    |                |
| dream_content     | text       | YES  |     | NULL    |                |
| we_chat_name      | char(50)   | YES  |     | NULL    |                |
| dream_date        | char(20)   | YES  |     | NULL    |                |
| dream_finish_date | char(20)   | YES  |     | NULL    |                |
| dream_uuid        | char(20)   | YES  |     | NULL    |                |
+-------------------+------------+------+-----+---------+----------------+
```
笑话表（joke）结构：
```
+---------------+------------+------+-----+---------+----------------+
| Field         | Type       | Null | Key | Default | Extra          |
+---------------+------------+------+-----+---------+----------------+
| joke_id       | bigint(20) | NO   | PRI | NULL    | auto_increment |
| joke_net_site | char(150)  | YES  |     | NULL    |                |
| joke_content  | text       | YES  |     | NULL    |                |
| joke_date     | char(20)   | YES  |     | NULL    |                |
+---------------+------------+------+-----+---------+----------------+
```
笑话更新历史表（jokehistory）结构：
```
+------------------+------------+------+-----+---------+----------------+
| Field            | Type       | Null | Key | Default | Extra          |
+------------------+------------+------+-----+---------+----------------+
| history_id       | bigint(20) | NO   | PRI | NULL    | auto_increment |
| history_net_site | char(150)  | YES  |     | NULL    |                |
| history_date     | char(20)   | YES  |     | NULL    |                |
+------------------+------------+------+-----+---------+----------------+
```
## 更新日志

### 2018.01.02<br>
删除梦想需要根据id及昵称来删除，需要确定不可以删除别人的梦想<br>
增加梦想完成日期<br>
增加每天梦想提示<br>
增加测试模式标记<br>
系统配置项与运行步骤<br>

## 问题
提示信息的多样化处理

## 实例演示

### 1.进入梦想号

输入任何文字内容发送后，即可进入梦想号

![](/img/enter_dream_plane.png)

### 2.放飞梦想
按“A_梦想名_梦想内容”这个格式输入梦想，点击发送，即可放飞梦想

![](/img/fly_my_dream.png)

### 3.修改查询梦想
按"M_梦想ID_梦想名_梦想内容"这个格式输入修改数据，发送即可修改您的梦想

![](/img/modify_query_my_dream.png)

### 4.完成删除梦想
按“F_梦想ID“格式完成梦想，完成梦想后，梦想号不再会第天提醒您<br>
按”D_梦想ID“格式删除梦想，删除梦想后，你的梦想将化为泡影消失的无影无踪

![](/img/finish_delete_my_dream.png)

### 5.梦想号提示
梦想号第天对您的梦想进行提示
![](/img/dream_plane_hint1.png)

### 6.梦想号测试模式下5分钟提示一次，正常情况下是每天只提示一次
![](/img/dream_hint_5_mins.png)

### 视频观看

请您移步vedio目录下
[](https://github.com/shenjianli/DreamServer/blob/master/video/Dream_WeChat.mp4)
