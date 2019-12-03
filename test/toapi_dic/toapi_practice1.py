# encoding:utf-8
'''
Toapi 是一个能够将任何 web 网站转化为 api 服务的库。

这是一个让所有网站都提供API的Python库。以前，我们爬取数据，然后把数据存起来，再创造一个api服务以便其他人可以访问。为此，我们还要定期更新我们的数据。
这个库让这一切变得容易起来。你要做的就是定义好你的数据，然后这些数据就会自动地变成可以访问的API。
'''
from flask import request
from htmlparsing import Attr, Text
from toapi import Api, Item

api = Api()

@api.site('http://www.itest.info')
@api.list('.col-md-3')
@api.route('/courses?page={page}', '/courses')
@api.route('/courses', '/courses')
class Course(Item):
    url = Attr('a', 'href')
    title = Text('h4')

api.run(debug=True, host='0.0.0.0', port=12306)