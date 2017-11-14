#-*- coding: utf-8 -*-

'''
该module主要负责实现html静态文件的组装
生成一套基本模板，在此基础上利用HtmlObject
的toHtmlElement方法得到的元素插入模板中
'''

from media import Movie

class HtmlCreator:
    @staticmethod
    def create(movies):
        head = '<!DOCTYPE html><html><body>'
        tail = '</body></html>'
        body = '''
        <p>这是第一个段落。</p>
        '''
        return head + body + tail
