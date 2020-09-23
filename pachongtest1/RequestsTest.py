import re

import requests
import logging
from loggingconfig import config
from MySql import connect

url = 'https://www.baidu.com'
response = requests.get(url)
if response.status_code == 200:
    print(response.text)


def getStr(str):
    return re.findall('\d', str)





def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        logging.error(e)
        return None

def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dangdang(url)
    result = parse_result(html)
    return result

if __name__ == '__main__':
    access = connect.DataBaseAccess()
    for x in range(1,10):
        dict = next(main(x))
        access.insertDatas2(dict)
