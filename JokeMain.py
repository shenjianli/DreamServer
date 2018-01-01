#!/usr/bin/python3

# 笑话集中营
import requests         # 导入requests库
import re               # 导入正则表达式库
import JokeDB
import UpdateDB
domain = 'http://www.jokeji.cn'


def repleac_exception_str(joke):
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


def print_joke(joke):
        if "<BR>" in joke:
                joke_array = joke.split("<BR>")
                for context in joke_array:
                        print(context)
        else:
                print(joke)


def find_jokes(content):
        reg = r'<P>[0-9]、(.+?)</P>'
        joke_re = re.compile(reg)
        jokes = re.findall(joke_re, content)
        return jokes


def search_jokes_by_link(link_url):
        joke_content = requests.get(link_url)  # 访问第一个链接
        joke_content.encoding = 'gbk'
        return joke_content.text


def get_joke_list(joke_text):
        joke_list = re.findall('/jokehtml/[\w]+/[0-9]+.htm', joke_text)  # 使用正则表达式找到所有笑话页面的链接
        return joke_list


def get_joke_page():
        print();


if __name__ == '__main__':

        jokePage = requests.get('http://www.jokeji.cn/list.htm')
        #jokePage = requests.get('http://www.jokeji.cn/list_1.htm')
        jokePage.encoding = 'gbk'

        jokeList = get_joke_list(jokePage.text)  # 使用正则表达式找到所有笑话页面的链接

        UpdateDB.open_db()
        # 查询最近更新的地址
        last_site = UpdateDB.query_mysql_data()
        print("最近更新的地址是：", last_site)
        req_list = []
        for site in jokeList:
                if site != last_site:
                        req_list.append(site)
                else:
                        break
        if len(req_list) != 0:
                # 更新最近更新地址数据
                UpdateDB.insert_mysql_data(req_list[0])
                print("本次需要更新的地址：", req_list)
        else:
                print("已经为最新了，不需要更新了")

        # 遍历请求需要爬取的数据
        for jokeLink in req_list:

                link = domain + jokeLink

                # 爬取指定地址的具体内容
                content = search_jokes_by_link(link)
                # 从具体内容中获取笑话集合数据
                jokes = find_jokes(content)

                # 循环打印笑话，并存入数据库
                for joke in jokes:
                        # 替换异常字符
                        joke_no_except = repleac_exception_str(joke)
                        JokeDB.open_db()
                        # 数据库中插入数据
                        JokeDB.insert_mysql_data(link, joke_no_except)
                        # 打印笑话
                        print_joke(joke_no_except)
                        # 打印一个换行
                        print()
        #关闭数据库
        JokeDB.close_joke_db()
        UpdateDB.close_joke_db()


        # for jokeLink in jokeList:
        #         jokeContent = requests.get('http://www.jokeji.cn/' + jokeLink)      # 访问第一个链接
        #         jokeContent.encoding = 'gbk'
        #         jokes = re.findall('<P>[0-9].*</P>', jokeContent.text)
        #         for joke in jokes:          # 循环打印笑话
        #                 print(joke)
        #                 print()                 # 打印一个换行

