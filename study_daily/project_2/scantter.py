#-*- coding: utf-8 -*-

'''
该module主要负责根据关键字去豆瓣爬取相关电影信息
并组装创建一个Movie对象
'''

from media import Movie

import urllib
import json
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

def get(key):
    response = urllib.urlopen('https://api.douban.com/v2/movie/search?q='+ key +'&count=3')
    html = response.read()
    jsonMap = json.loads(html)
    movies = []
    for subject in jsonMap['subjects']:
        movie = Movie(
                subject['title'],#电影标题
                subject['rating']['average'],#电影评分
                subject['rating']['stars'],#星星数
                subject['collect_count'],#电影收藏次数
                subject['genres'],#电影分类
                subject['casts'],#电影主演
                subject['directors'],#电影导演
                subject['year'],#上映时间
                subject['images']['medium']#电影海报
                )
        movies.append(movie)

    return movies if len(movies) > 0 else None


if __name__ == '__main__':
    movies = get('我是')
    for movie in movies:
        print movie
        for genre in movie.genres:
            print genre
        for cast in movie.casts:
            print cast
        for director in movie.directors:
            print director
