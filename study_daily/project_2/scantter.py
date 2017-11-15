#-*- coding: utf-8 -*-

'''
该module主要负责根据关键字去豆瓣爬取相关电影信息
并组装创建一个Movie对象
'''

from media import Movie

import urllib
import json
import sys
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf-8')

search_count = 5

def get(key):
    response = urllib.urlopen('https://api.douban.com/v2/movie/search?q='+ key +'&count=' + str(search_count))
    html = response.read()
    jsonMap = json.loads(html)
    movies = []
    for subject in jsonMap['subjects']:
        alt = subject['alt']
        play_url = 'http://v.youku.com/v_show/id_XMjg0ODU2MDY4MA==.html?spm=a2hww.20027244.ykRecommend.5~5!2~5~5~A'
        movie = Movie(
                subject['title'],#电影标题
                subject['rating']['average'],#电影评分
                subject['rating']['stars'],#星星数
                subject['collect_count'],#电影收藏次数
                subject['genres'],#电影分类
                subject['casts'],#电影主演
                subject['directors'],#电影导演
                subject['year'],#上映时间
                subject['images']['medium'],#电影海报
                play_url
                )
        movies.append(movie)

    return movies if len(movies) > 0 else None


if __name__ == '__main__':
    '''
    movies = get('我是')
    for movie in movies:
        print movie
        for genre in movie.genres:
            print genre
        for cast in movie.casts:
            print cast
        for director in movie.directors:
            print director
    '''
    res = urllib.urlopen('http://www.chapaofan.com/search/猩球')
    soup = BeautifulSoup(res.read(), 'lxml')
    # filter with class='item'
    items = soup.select('.item')
    for item in items:
        second_a = item.select('a')[1]
        second_a_img = second_a.select('img')[0]
        first_span = item.select('span')[0]
        five_li = item.select('li')[4]
        six_li = item.select('li')[5]
        print second_a
        print first_span
        print five_li
        print six_li
        # get video title
        title = second_a['title']
        print title
        # get poster image url
        poster_image_url = second_a_img['data-original']
        print poster_image_url
        # get score
        score = float(first_span.string)
        print str(score)
        # get country
        country = five_li.string
        print country
        # get category
        category = six_li.string
        print category
        # get video play outside url
        outside_url = second_a['href']
        print outside_url
        #res_outside = urllib.urlopen(outside_url)
        #soup_play = BeautifulSoup(res_outside.read(), 'lxml')
