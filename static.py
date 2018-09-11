# -*- coding: utf-8 -*-
# filename: index_page.py

import hashlib
import web
import os
from my_log import debug_print

class static(object):
    def GET(self, filename):
        if os.path.exists("./css/" + filename):
            return open("./css/" + filename).read()
        else:
            return ""
