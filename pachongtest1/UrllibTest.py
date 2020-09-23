import bs4
import requests
from selenium import webdriver

if __name__ == '__main__':

    str1 = 'a  b c d'
    print(str1.replace(' ', ''))

    print(type(str(25)))
    list = ["a", 1]
    print(list[0])
    # for x in list:
    # print(x)
    dict = {"k1": "v1", "k2": 2}
    print(dict.get("k2"))
    print(float("29.32"))
    url = 'https://www.baidu.com'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        # print(html)
        soup = bs4.BeautifulSoup(html, 'lxml')
        # print(soup.a.string)

    html_doc = """

    <html><head><title>学习python的正确姿势</title></head>
    <body>
    <p class="title"><b>小帅b的故事</b></p>

    <p class="story">有一天，小帅b想给大家讲两个笑话
    <a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
    <a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
    他问大家，想听长的还是短的？</p>

    <p class="story">...</p>

    """

    html = """

    <html><head><title>The Dormouse's story</title></head>

    <body>

    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were

    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and


    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;

    and they lived at the bottom of a well.</p>

    <p class="story">...</p>

    """
    soup = bs4.BeautifulSoup(html, 'lxml')
    p_children = soup.p.children
    for x in p_children:
        print(x)
    print('----------------')
    print(soup.a.text)
    print(soup.findAll(class_='sister'))
    p_all = soup.find_all('a')
    if p_all is not None:
        for p in p_all:
            pass
            # print(p)

    douban_html = '''
                <li>
                <div class="item">
                <div class="pic">
                <em class="">26</em>
                <a href="https://movie.douban.com/subject/1296141/">
                <img alt="控方证人" class="" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1505392928.jpg" width="100"/>
                </a>
                </div>
                <div class="info">
                <div class="hd">
                <a class="" href="https://movie.douban.com/subject/1296141/">
                <span class="title">控方证人</span>
                <span class="title"> / Witness for the Prosecution</span>
                <span class="other"> / 雄才伟略  /  情妇</span>
                </a>
                <span class="playable">[可播放]</span>
                </div>
                <div class="bd">
                <p class="">
                                            导演: 比利·怀尔德 Billy Wilder   主演: 泰隆·鲍华 Tyrone Power / 玛琳·...<br/>
                                            1957 / 美国 / 剧情 犯罪 悬疑
                                        </p>
                <div class="star">
                <span class="rating5-t"></span>
                <span class="rating_num" property="v:average">9.6</span>
                <span content="10.0" property="v:best"></span>
                <span>312122人评价</span>
                </div>
                <p class="quote">
                <span class="inq">比利·怀德满分作品。    </span>
                </p>
                </div>
                </div>
                </div>
                </li>
    '''
    soup1 = bs4.BeautifulSoup(douban_html, 'lxml')
    # 电影排名
    rank = soup1.em.string
    print(rank)
    # 电影名称
    movieName = soup1.findAll(class_='title')[0].string
    # for name in movieName:
    #     print(name)
    print(movieName)
    # 电影图片
    moviePic = soup1.img.get('src')
    print(moviePic)
    # 电影简介
    jianjie = soup1.p.text.replace(' ', '')
    print(jianjie)
    # 电影评分
    score = soup1.find(class_='rating_num').string
    print(score)
    # 电影作者
    author = soup1.find(class_='inq').text
    print(author)

    list = [['a',1],['b',2]]
    for l in list:
        print(type(l))