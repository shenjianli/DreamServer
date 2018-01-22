## 梦想号演示

### 简介
梦想号@B2C项目（张勇、徐达、董亚、申建利）

### 视频地址

### 创作理念

#### 1.为了心中有梦

现象：许多人说A寺许愿很灵验，所以我们都去A寺去许愿，果不其然，我们实现了我们的愿望
原因：难道是A寺真的灵验么？最终我找到了答案，原因是在A寺许的愿望，在他的心中存留的时间较长，实现的梦想的概率也就越大

为了我们心中有梦，所以梦想号每天进行梦想提醒

#### 2.为了立长志

现象：今天许下了梦想，过一段时间已经忘记了原来许的梦想，又重新许下新的梦想，周而复始，总是在许梦想，却从未真正拥有过梦想 ----  "有志之人立长志，无志之人常立志"

为了立长志，为了真正拥有梦想，所以出现了梦想号

#### 3.为了梦想不再孤单

现象：由于没有陪伴，梦想夭折在实现的道路上

为了梦想不再孤单，所以梦想号将在你实现梦想的道路上，与你一路同行（通过提醒，及用户对你梦想的点赞，加油语）


### 技术亮点

#### 1.Python爬虫  ----  我要和没有数据的日子说再见

Python爬虫例子代码：
```
# 替换一些异常信息
def repleace_exception_str(joke):
        if '&nbsp;' in joke:
                joke = joke.replace('&nbsp;', '')

        if '<A' in joke and '</A>' in joke:
                start = joke.index('<A')
                end = joke.index('</A>')
                exception_str = joke[start:end + 4]
                joke = joke.replace(exception_str, '')

        if '<IMG' in joke and '0>' in joke:
                start = joke.index('<IMG')
                end = joke.index('0>')
                img_str = joke[start:end + 2]
                joke = joke.replace(img_str, '')

        if '@' in joke:
                start = joke.index('@')
                author = joke[start]
                joke = joke.replace(author, '')

        if '“' in joke:
                joke = joke.replace('“', ' ')

        if '”' in joke:
                joke = joke.replace('”', ' ')
        if '"' in joke:
                joke = joke.replace('"', ' ')

        return joke

# 打印笑话信息
def print_joke(joke):
        if "<BR>" in joke:
                joke_array = joke.split("<BR>")
                for context in joke_array:
                        print(context)
        else:
                print(joke)

# 根据网页内容匹配指定的笑话信息
def find_jokes(content):
        reg = r'<P>[0-9]、(.+?)</P>'
        joke_re = re.compile(reg)
        jokes = re.findall(joke_re, content)
        return jokes

# 通过url地址来搜索页面的文本信息
def search_jokes_by_link(link_url):
        joke_content = requests.get(link_url)  # 访问第一个链接
        joke_content.encoding = 'gbk'
        return joke_content.text

# 根据网页上的信息获取链接地址
def get_joke_list(joke_text):
        joke_list = re.findall('/jokehtml/[\w]+/[0-9]+.htm', joke_text)  # 使用正则表达式找到所有笑话页面的链接
        return joke_list
```

爬虫结果数据：

```
男子的去体检，医生说：小伙子，裤子脱了我看看你有没有女朋友。
男子裤子脱了。
医生说：你没女朋友吧。男子好奇：你怎么知道的？
医生说：看到纸屑了，来转过来，让我看看你有没有男朋友！


同桌戴着一条一块硬币做的吊坠。
我问他：为啥不戴金银不戴玉，偏偏戴了个硬币！
同桌：因为没有它就没有我，它是我的守护神！
我：这话怎么说？
同桌：当初，我妈要用这硬币买套，却被我爸偷偷藏了起来，于是，就有了我！
我：......


甲： 我跟我心目中的女神表白了。
乙： 那她同意没有啊？
甲： 诶，同意了。 　
乙： 那是好事啊，干嘛唉声叹气的.....
甲： 我当时大义凌然地说，有种，你就嫁给我。
乙： 嗯，虽不浪漫，但也够霸气的了，她怎么说啊？
甲： 我还真有了，不过不是你的。
乙：......


过节公司加餐，饭后又发一苹果。
下午饿了，拿出苹果正啃得高兴，被综管部拍照罚了两百。
我： 公司发的苹果，就在公司吃，怎么了？
综管领导: 公司发的钱，你怎么不全在公司花完？


表弟在公司推广的 光盘行动 中，连三天得了第一，他说把饭菜都能吃个精光。
我表示不信，说菜要是有骨头，鱼刺你也能吃掉？
表弟：说出来你不信，我在公司菜肴里，吃到最硬的东西就是花椒……


开会前，主任让我给他写演讲稿，主任强调：这次会议的内容很重要，我说的每一句话，都要有特别的味道！
我说：全是屁话，能有什么特别的味道啊？
同事：那屁是什么味你自己心里没数啊？


同事受伤住院，我们几个人一起去探望，天气不错，我们推着轮椅带同事出门晒晒太阳。
同事是个乐观的人，跟我们说:不就这点小伤嘛，没事，看我坐坐轮椅给你们来个漂移……
现在我们都在重症监护室门口等着……


员工：老板，每次迟到什么的，你都是扣奖金，扣工资不一样吗？
老板：你的意思我明白。不就是工资给老婆，奖金归你吗？
员工：是啊，老板，那能不能改一下？
老板：不行！
员工：为啥不行啊？
老板：你以为我没老婆，公司的钱我老婆管着，只有奖金是由我支配，从你们身上扣下的，我就可以攒点零花钱！
```

#### 2.微信仿小艾智能提醒 ----  哈哈，再也不会因为忘记重要日子，回家跪键盘啦

微信提醒代码：

```
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
```

微信提醒效果：

![](/img/dream_hint_5_mins.png)

#### 3.RxAndroid RxJava   -----  快速线程切换，使你再也不怕UI卡顿啦

线程切换代码：
```
jokeApi.updateJokeBaseInfo(lastId, num).map(new HttpResultFunc<List<Joke>>())
  .map(new Func1<List<Joke>, Boolean>() {
       @Override
       public Boolean call(List<Joke> jokes) {
           if (null != jokes && jokes.size() > 0) {
               JokeDao jokeDao = DreamApp.getDreamApp().getDaoSession().getJokeDao();
               if (null != jokeDao) {

                   for (Joke joke : jokes) {
                       LogUtils.i("收到的笑话数据：" + joke.toString());
                       jokeDao.insertWithoutSettingPk(joke);
                   }

                   Joke update = jokes.get(0);
                   long updateId = update.getId();
                   SharedPreUtils.put(context, Constants.DATA_UPDATE_ID, String.valueOf(updateId));

                   HistoryDao historyDao = DreamApp.getDreamApp().getDaoSession().getHistoryDao();
                   History history = new History();
                   history.setUpDate(update.getDate());
                   SimpleDateFormat sDateFormat = new SimpleDateFormat("yyyy-MM-dd");
                   String nowDate = sDateFormat.format(new java.util.Date());
                   history.setHisDate(nowDate);
                   historyDao.insertWithoutSettingPk(history);
                   SharedPreUtils.put(context, Constants.DATA_UPDATE_DATE, nowDate);


                   Thread thread = Thread.currentThread();
                   LogUtils.i("当前线程名：" + thread.getName());
                   return true;
               }
           }
           return false;
       }
   })
   .subscribeOn(Schedulers.io())
   .unsubscribeOn(Schedulers.io())
   .observeOn(AndroidSchedulers.mainThread())
   .subscribe(jokeSubscriber);
```

#### 4.本地MockService -----   实现Android前台开发与后台的完美分离，妈妈再也不用担心我的开发了

MockService代码：

```
public class DreamMockTxtService extends MockService{
    @Override
    public String getJsonData() {
        String resultStr =  MockUtils.readFromRaw(DreamApp.getDreamApp(), R.raw.dream_json);
        LogUtils.i("获得的json字符串为：" + resultStr);
        return resultStr;
    }
}
```
其中使用的dream_json如下：

```
{
	"code": 1,
	"msg": "查询成功",
	"data": [{
		"id": 1,
		"name": "2018技术",
		"content": "希望自己在2018年，可以在Android技术方面上一个大台阶",
		"nick": "JerryShen",
		"date": "2018-01-02 10:11:38"
	}, {
		"id": 2,
		"name": "艾融梦",
		"content": "看互联网金融，问苍茫大地，谁主沉浮？数风流人物，还看今朝",
		"nick": "Jerry",
		"date": "2018-01-02 10:27:13"
	}, {
		"id": 3,
		"name": "写博客",
		"content": "每个月写一篇有技术含量的博客",
		"nick": "Jerry",
		"date": "2018-01-02 13:40:33"
	}, {
		"id": 4,
		"name": "开源库",
		"content": "今年写一个好的Android开源库，星数达到1000星",
		"nick": "JerryShen",
		"date": "2018-01-02 13:40:33"
	}, {
		"id": 5,
		"name": "梦想",
		"content": "理想是力量的泉源、智慧的摇篮、冲锋的战旗、斩棘的利剑",
		"nick": "JerryShen",
		"date": "2018-01-02 13:40:33"
	}]
}
```

[使用详情](https://github.com/shenjianli/LibTest)

### 笨鸟助手  -----  自从使用它，经理再也不用担心，我忘记签到，签退啦

大赛终点也是新的起点

每天在指定的时间点，会发送一条微信给用户，提醒用户进行签到，签退，打卡操作

笨鸟提醒效果图：

![](/img/sign_in_out.png)


[使用详情](https://github.com/shenjianli/DialyHelper)

目前正在内部测试阶段，欢迎大家报名试用，谢谢！

### 结束

有志者事竞成，破釜沉舟，百二秦关终属楚

苦心人天不负，卧薪尝胆，三千越甲可吞吴

祝大家在新的一年里，美梦成真，在梦想的道路上一帆风顺

## 赞赏

![](/img/we_chat.png)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ![](/img/alipay.png)