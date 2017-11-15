# project 2 read me

### 运行该项目
1. 需要安装有beautifulsoup库
2. python entertainment_center.py
3. 输入喜欢的电影名（支持模糊），并使用中文逗号分割，回车结束
4. 打开fresh_tomotoes.html

### 功能实现流程分析
1. 接受用户输入喜爱的电影名，逗号分割
2. 使用爬虫爬取豆瓣搜索该电影的信息（因豆瓣无法很好的保证有播放地址，后修改为从泡饭影视拉取）
3. 提取其中我们需要的信息生成对应的Movie对象
4. 调用fresh_tomotoes.py方法生成html静态页面文件

### 项目提交
在这个项目中，你将用编写代码，存储你最喜爱的电影信息，包括剧照和电影预告片网址。
然后编写一个静态网页，允许网页访客浏览电影和观看预告片。

我该如何完成这个项目？
1. 创建一个数据结构（即 Python 类）来存储你最喜爱的电影，包括电影片名、
剧照网址（或海报网址）以及电影预告片的 YouTube 链接。
2. 创建该 Python 类的多个实例来代表你最喜爱的电影；将所有实例放在一个列表中。
3. 为帮助你生成一个显示这些电影的网站，我们提供了一个名为 fresh_tomatoes.py 的 
Python 模块 - 此模块有一个名为 open_movies_page的函数，它将一个参数作为输入，
即电影列表，然后创建一个 HTML 文件来可视化你最喜爱的所有电影。 
（ 2017年11月13日更新：这个fresh_tomatoes.py同时兼容 YouTube 和 Youku 的链接，
需要把你自己的 Movie 类中 trailer_youtube_url 属性改成 trailer_url）
4. 确保在浏览器中加载你的网站时，它能正确渲染。
对于这个项目，你需要提交一个命名为 movie_website.zip 的项目压缩文件。
此压缩文件应该包含三个 Python 文件：media.py、entertainment_center.py 和 fresh_tomatoes.py。



### 工程中参考文档：
1. 豆瓣API https://developers.douban.com/wiki/?title=movie_v2#search
2. 发现使用豆瓣播放是个问题，豆瓣网页中不一定有播放链接
3. 现修改为从泡饭影视网站拉取数据 http://www.chapaofan.com/4505.html http://player.youku.com/jsapi
4. 参考一篇beautifulsoup的博客 http://cuiqingcai.com/1319.html
