#-*- coding: utf-8 -*-

"""
该Module主要负责电影实体类，演员类，导演类，以及用于实现toHtmlElement方法的父类
"""

from abc import ABCMeta, abstractmethod
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlObject:
    """
    This class is a parent class for create html code.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def toHtmlElement(self):pass

class Cast(HtmlObject):
    """
    This class is for save cast info, and extends HtmlObject to have toHtmlObject function.

    Members:
        TYPE - class attribute，value is cast.
        name - instance attribute, save cast name.
        avatars - instance attribute, save cast avatars.
        alt - instance attribute, save cast alt.
    """
    TYPE = 'cast'

    def __init__(self, name, avatars, alt):
        self.name = name
        self.avatars = avatars
        self.alt = alt

    def __str__(self):
        return '{name:' + self.name +',type:' + Cast.TYPE + ',avatars:' + self.avatars + ',alt:' + self.alt + '}'

    def toHtmlElement(self):
        """
        This function to create a html element(Now do nothing).
        """
        return '<a></a>'

class Director(HtmlObject):
    """
    This class is for save director info, and extends HtmlObject to have toHtmlObject function.

    Members:
        TYPE - class attribute，value is director.
        name - instance attribute, save director name.
        avatars - instance attribute, save director avatars.
        alt - instance attribute, save director alt.
    """
    TYPE = 'director'

    def __init__(self, name, avatars, alt):
        self.name = name
        self.avatars = avatars
        self.alt = alt

    def __str__(self):
        return '{name:' + self.name +',type:' + Director.TYPE + ',avatars:' + self.avatars + ',alt:' + self.alt + '}'

    def toHtmlElement(self):
        """
        This function to create a html element(Now do nothing).
        """
        return '<a></a>'

class Movie:
    """
    This class is for save movie info.

    Members:
        title - instance attribute, save movie title.
        score - instance attribute, save movie score.
        stars - instance attribute, save movie stars.
        collect_count - instance attribute, save movie collect_count.
        genres - instance attribute, save movie genres.
        year - instance attribute, save movie year.
        poster_image_url - instance attribute, save movie poster_image_url.
        trailer_url - instance attribute, save movie trailer_url.
        casts - instance attribute, save movie casts.
        directors - instance attribute, save movie directors.
    """
    def __init__(self, title, score, stars, collect_count, genres, _casts, _directors, year, poster_image_url, trailer_url):
        self.title = title
        self.score = score
        self.stars = stars
        self.collect_count = collect_count
        self.genres = genres
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
        self.casts = []
        for cast in _casts:
            if cast['name'] is None or cast['avatars'] is None or cast['alt'] is None \
                or cast['avatars']['medium'] is None:continue
            self.casts.append(Cast(cast['name'], cast['avatars']['medium'], cast['alt']))
        self.directors = []
        for director in _directors:
            if director['name'] is None or director['avatars'] is None or director['alt'] is None \
                or director['avatars']['medium'] is None:continue
            self.directors.append(Director(director['name'], director['avatars']['medium'], director['alt']))

    def __str__(self):
        return '{title:' + self.title + ',score:' + str(self.score) + ',stars:' + str(self.stars) \
            + ',year:' + str(self.year) + ',trailer_url:' + self.trailer_url + '}'

