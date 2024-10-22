#!/usr/bin/env python
# -*- coding:utf-8 -*-

# DrissionPage 库 文档地址 http://g1879.gitee.io/drissionpagedocs/

#-导入库
from DrissionPage import ChromiumPage,ChromiumOptions

#-配置类
class Config:
    UA_android="Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36"
    UA_apple="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    url='https://gitee.com/g1879/DrissionPage'
    port=7878


#-创建配置对象
co=ChromiumOptions()

#-启动配置
co.set_local_port(Config.port)
co.ignore_certificate_errors(True)

#-创建浏览器
page = ChromiumPage(addr_or_opts=co)
#-创建标签页
tab=page.new_tab()



#-打开网址
tab.get(Config.url)

input('go on ?')
  