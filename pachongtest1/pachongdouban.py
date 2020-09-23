import requests
from bs4 import BeautifulSoup
from MySql import connect


def main(page):
    list = []
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response is not None and response.status_code == 200:
        html = response.text
        if html is not None:
            soup = BeautifulSoup(html, 'lxml')
            all = soup.find(class_='grid_view').find_all('li')
            for li in all:
                # print(li, end='\n')
                result = parseHtml(li)
                list.append(result)

    return list

def parseHtml(soup1):
    list = []
    # 电影排名
    rank = soup1.em.string
    list.append(rank)
    # print(rank)
    # 电影名称
    movieName = soup1.find(class_='title').string
    list.append(movieName)
    # print(movieName)
    # 电影图片
    moviePic = soup1.img.get('src')
    list.append(moviePic)
    # print(moviePic)
    # 电影简介
    jianjie = soup1.p.text.replace(' ', '')
    list.append(jianjie)
    # print(jianjie)
    # 电影评分
    score = soup1.find(class_='rating_num').string
    list.append(score)
    # print(score)
    # 电影作者
    author = soup1.find(class_='inq').string
    list.append(author)
    # print(author)
    return list


if __name__ == '__main__':
    list = []
    for page in range(0, 101, 25):
        result = main(page)
        # print(result)
        list.append(result)
    print('----')
    print(len(list))
    print((list[1]))
    connect.DataBaseAccess().insertDatasDouBan((list[1]))

