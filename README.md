# pagination
Django2.2 + python3.7 在网页中实现分页

将 utils、static 文件夹放入 project 下

url.py:
```
from django.urls import re_path
from app名 import views中的函数名

urlpatterns = [
    re_path(r'^你的地址-(?P<page>\d+).html$', views.page),
]
```
views.py:
```
from utils import paginations

# data_list 是所有数据
total_data = len(data_list)  # 总数据长度
# 获取当前页
current_page = kwargs.get('page', 1)
current_page = int(current_page)
# 分页
page_obj = paginations.Page(current_page, total_data, 'page')   # 实例化Page类（实例化参数介绍在utils/pagination中）
if current_page > page_obj.total_page_num:
    return HttpResponse('Page not found')
page_str = page_obj.page_str    # page_str 是生成的页码的html
data = data_list[page_obj.start_data: page_obj.end_data]    # 当前页面显示的数据
return render(request, 'page.html', {'data': data, 'page_list': page_str})
```
page.html:
```
<body>
<ul>
    {% for item in data %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
<div>{{ page_list }}</div>
<script src="/static/jQuery3.4.1.js"></script>
<script src="/static/page_jump.js"></script>
</body>
```
