# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
import ghost

# print(dir(ghost))
# print(dir(ghost.Ghost()))
# print dir(ghost.Ghost()

from ghost import Ghost
ghost = Ghost()
with ghost.start() as session:
    page, extra_resources = session.open("http://www.baidu.com")
    if page.http_status == 200 and 'CAPTCHA' in page.content:
    	print(page.content)

    print(page.content)