from flask import Flask, request
import JokeDB
import json
import DreamDB
import CoupletDB
import Config

app = Flask(__name__)


# 根url显示返回的信息
@app.route('/')
def hello_world():
    return '欢迎搭乘梦想号，我们将竭诚为您服务！'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


# 查询所有笑话数据
@app.route('/joke/query')
def query_joke_json():
    joke = JokeDB.query_mysql_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 根据日期查询笑话数据
@app.route('/joke/query_by_date')
def query_joke_by_date_json():
    date = request.args.get('date')
    joke = JokeDB.query_mysql_data_by_date(date)
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 更新笑话的基本信息
@app.route('/joke/query/base')
def query_joke_by_num_json():
    num = int(request.args.get('num'))
    joke = JokeDB.query_mysql_data_by_num(num)
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 根据上次请求id来更新笑话数据
@app.route('/joke/update')
def update_joke_by_json():

    lastId = int(request.args.get('lastId'))
    num = int(request.args.get('num'))

    count = JokeDB.query_joke_data_count()

    diff = count - lastId
    if lastId == 0 or diff >= 100:
        joke = JokeDB.query_mysql_data_by_num(100)
    else:
        joke = JokeDB.query_joke_data_by_id(lastId)

    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 根据url查询梦想数据，返回json字符串
@app.route('/dream/query')
def query_dream_json():
    joke = DreamDB.query_dream_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 根据url查询对联返回json字符串
@app.route('/couplet/query')
def query_couplet_json():
    joke = CoupletDB.query_couplet_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 根据请求增加梦想
@app.route('/add/dream')
def add_dream():

    result_str = ''
    result_code = 0
    result_msg = '查询成功'
    name = request.args.get('name')
    content = request.args.get('content')
    nick = request.args.get('nick')
    print("增加梦想接口收到数据：", name, content,nick)
    if name == '' or content == '' or name is None or content is None:
        result_msg = '梦想名或梦想内容不能为空'
    elif nick != '' and nick is not None:
        dream_id = DreamDB.insert_dream_data(name, content, nick)
        if dream_id != '' and dream_id is not None:
            result_msg = '加入梦想成功'
            result_str = dream_id
            result_code = 1
            print('加入梦想成功')

    else:
        result_msg = '昵称不能为空'

    result = {}

    result['code'] = result_code
    result['msg'] = result_msg
    result['data'] = result_str

    joke_json = json.dumps(result, ensure_ascii=False)
    print(joke_json)
    return joke_json


# 主方法
if __name__ == '__main__':
    #app.config['SERVER_NAME'] = 'i2finance.dream.com'
    # 表示主机地址与端口号
    app.run(host=Config.dream_server_site, port=Config.dream_server_port)
