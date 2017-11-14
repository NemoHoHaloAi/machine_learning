# project 2 read me
```
1. 接受用户输入喜爱的电影名，逗号分割
2. 使用爬虫爬取豆瓣搜索该电影的信息
3. 提取其中我们需要的信息生成对应的Movie对象
4. 调用Movie对象的toHtml方法填充到模板文件中
5. 基类:HtmlParent，只有一个方法toHtml
6. 子类:Movie.....

项目提交

在这个项目中，你将用编写代码，存储你最喜爱的电影信息，包括剧照和电影预告片网址。
然后编写一个静态网页，允许网页访客浏览电影和观看预告片。

我该如何完成这个项目？
如果你还没有安装 Python，请下载安装
创建一个数据结构（即 Python 类）来存储你最喜爱的电影，包括电影片名、
剧照网址（或海报网址）以及电影预告片的 YouTube 链接。
创建该 Python 类的多个实例来代表你最喜爱的电影；将所有实例放在一个列表中。
为帮助你生成一个显示这些电影的网站，我们提供了一个名为 fresh_tomatoes.py 的 
Python 模块 - 此模块有一个名为 open_movies_page的函数，它将一个参数作为输入，
即电影列表，然后创建一个 HTML 文件来可视化你最喜爱的所有电影。 
（ 2017年11月13日更新：这个fresh_tomatoes.py同时兼容 YouTube 和 Youku 的链接，
需要把你自己的 Movie 类中 trailer_youtube_url 属性改成 trailer_url）
确保在浏览器中加载你的网站时，它能正确渲染。
对于这个项目，你需要提交一个命名为 movie_website.zip 的项目压缩文件。
此压缩文件应该包含三个 Python 文件：media.py、entertainment_center.py 和 fresh_tomatoes.py。
```
