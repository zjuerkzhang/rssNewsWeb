# -*- coding: utf-8 -*-
# filename: index_page.py

import hashlib
import web
import os
from my_log import debug_print
g_selected_book_dir = "/var/www/news/"

class index_page(object):
    def GET(self):
        html_files = []
        render = web.template.render('templates')
        file_list = os.listdir(g_selected_book_dir)
        file_list = filter(lambda x:x.find('.html')>=0 , file_list)
        file_list.sort(reverse=True)
        html_files = map(lambda x: {'name': x.replace('.html', '').replace('daily_', ''), 'link': './raw/' + x}, file_list)
        latest_content = ''
        data = {'file_list': html_files, 'latest': latest_content}
        return render.index(data)
