# DreamServer

## 命令使用

### 放飞梦想
A_梦想名_梦想内容

### 删除梦想
D_梦想ID

### 修改梦想
M_梦想ID_梦想名_梦想内容

### 查询梦想
Q_梦想ID

### 完成梦想
F_梦想ID

## 运行

### 1.安装mysql数据库

### 2.配置mysql数据库
#### 2.1 创建数据库
使用命令 create database dream
#### 2.2 配置数据库
打开Config.py文件内容如下

```
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

# 表示梦想号每天提示时间点
dream_hint_hour = 8
dream_hint_min = 30
```
进行相对应的配置即可

#### 2.3 创建数据表
执行DreamDB.py来创建数据表
可以使用命令 python DreamDB.py 来生成数据表

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
python FlaskServer.py
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


## 更新日志

2018.01.02
删除梦想需要根据id及昵称来删除，需要确定不可以删除别人的梦想
增加梦想完成日期
增加每天梦想提示
增加测试模式标记
系统配置项与运行步骤

## 问题
提示信息的多样化处理

