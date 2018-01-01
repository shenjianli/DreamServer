from flask import Flask,request
import JokeDB
import json
import DreamDB
import CoupletDB

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Shen!'


# http://127.0.0.1:5000/index/   #访问这个会报错的
@app.route('/index')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World'


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


@app.route('/joke/query')
def query_joke_json():
    joke = JokeDB.query_mysql_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


@app.route('/joke/query_by_date')
def query_joke_by_date_json():
    date = request.args.get('date')
    joke = JokeDB.query_mysql_data_by_date(date)
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


@app.route('/joke/query/base')
def query_joke_by_num_json():
    num = int(request.args.get('num'))
    joke = JokeDB.query_mysql_data_by_num(num)
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


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


@app.route('/dream/query')
def query_dream_json():
    joke = DreamDB.query_dream_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json

@app.route('/couplet/query')
def query_couplet_json():
    joke = CoupletDB.query_couplet_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return joke_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)