from django.utils.safestring import mark_safe


# 使用跳转需要在jQuery下导入 '/static/page_jump.js'
# 默认url为 '/url-1'
class Page(object):
    def __init__(self, current_page, total_data, url, data_num_per_page=10, page_num=7):
        self.current_page = current_page
        self.total_data = total_data
        self.url = url
        self.data_num_per_page = data_num_per_page
        self.page_num = page_num

    @property
    def start_data(self):
        return (self.current_page - 1) * self.data_num_per_page

    @property
    def end_data(self):
        return self.current_page * self.data_num_per_page

    @property
    def total_page_num(self):
        total_page_num, rest = divmod(self.total_data, self.data_num_per_page)
        if rest:
            return total_page_num + 1
        else:
            return total_page_num

    @property
    def page_str(self):
        page_list = []
        start_page = self.current_page - (self.page_num - 1) / 2
        end_page = self.current_page + (self.page_num - 1) / 2 + 1
        first_page = '<a class= "page" href="/%s-%d.html">%s</a><a>...</a>' % (self.url, 1, 1)
        last_page = '<a>...</a><a class= "page" href="/%s-%d.html">%s</a>' % (self.url, self.total_page_num,
                                                                              self.total_page_num)
        if start_page <= 1:
            start_page = 1
            end_page = 1 + self.page_num
            first_page = ''
        elif end_page >= self.total_page_num:
            start_page = self.total_page_num - self.page_num + 1
            end_page = self.total_page_num + 1
            last_page = ''
        # 上一页按钮
        if self.current_page > 1:
            temp = '<a class= "page" href="/%s-%d.html">%s</a>' % (self.url, self.current_page - 1, '上一页')
        else:
            temp = '<a class= "page" href="#">%s</a>' % '上一页'
        page_list.append(temp)
        # 第一页
        page_list.append(first_page)
        # 循环生成页码
        for i in range(int(start_page), int(end_page)):
            if i == self.current_page:
                temp = '<a class= "page active" href="/%s-%d.html">%d</a>' % (self.url, i, i)
            else:
                temp = '<a class= "page" href="/%s-%d.html">%d</a>' % (self.url, i, i)
            page_list.append(temp)
        # 最后一页
        page_list.append(last_page)
        # 下一页按钮
        if self.current_page < self.total_page_num:
            temp = '<a class= "page" href="/%s-%d.html">%s</a>' % (self.url, self.current_page + 1, '下一页')
        else:
            temp = '<a class= "page" href="#">%s</a>' % '下一页'
        page_list.append(temp)
        # 跳转框
        temp = '<input type="text"><a href="/%s-1.html" id="page_jump_tag">GO</a>' % self.url
        page_list.append(temp)
        page_str = ''.join(page_list)
        page_str = mark_safe(page_str)
        return page_str
