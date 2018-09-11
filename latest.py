# -*- coding: utf-8 -*-
# filename: index_page.py

import hashlib
import web
import os
from my_log import debug_print
g_selected_book_dir = "/var/www/news/"

class latest(object):
    def GET(self):
        html_files = {'selected': [], 'unselected': []}
        render = web.template.render('templates')
        file_list = os.listdir(g_selected_book_dir)
        file_list = filter(lambda x:x.find('.html')>=0 , file_list)
        file_list.sort()
        latest_file = file_list[-1]
        if ( not latest_file ):
            return "No Conetent"
        return open(g_selected_book_dir + latest_file, 'r').read()
