#-*- coding: utf-8 -*-

'''
该Module主要负责电影实体类，演员类，导演类，以及用于实现toHtmlElement方法的父类
'''

from abc import ABCMeta, abstractmethod
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlObject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def toHtmlElement(self):pass

class Cast(HtmlObject):
    TYPE = 'cast'

    def __init__(self, name, avatars, alt):
        self.name = name
        self.avatars = avatars
        self.alt = alt

    def __str__(self):
        return '{name:' + self.name +',type:' + Cast.TYPE + ',avatars:' + self.avatars + ',alt:' + self.alt + '}'

    def toHtmlElement(self):
        return '<a></a>'

class Director(HtmlObject):
    TYPE = 'director'

    def __init__(self, name, avatars, alt):
        self.name = name
        self.avatars = avatars
        self.alt = alt

    def __str__(self):
        return '{name:' + self.name +',type:' + Director.TYPE + ',avatars:' + self.avatars + ',alt:' + self.alt + '}'

    def toHtmlElement(self):
        return '<a></a>'

class Movie:
    def __init__(self, title, score, stars, collect_count, genres, _casts, _directors, year, poster):
        self.title = title
        self.score = score
        self.stars = stars
        self.collect_count = collect_count
        self.genres = genres
        self.casts = []
        for cast in _casts:
            if cast['name'] is None or cast['avatars'] is None or cast['alt'] is None or cast['avatars']['medium'] is None:continue
            self.casts.append(Cast(cast['name'], cast['avatars']['medium'], cast['alt']))
        self.directors = []
        for director in _directors:
            if director['name'] is None or director['avatars'] is None or director['alt'] is None or director['avatars']['medium'] is None:continue
            self.directors.append(Director(director['name'], director['avatars']['medium'], director['alt']))
        self.year = year
        self.poster = poster

    def __str__(self):
        return '{title:' + self.title + ',score:' + str(self.score) + ',stars:' + str(self.stars) + ',year:' + str(self.year) + '}'

