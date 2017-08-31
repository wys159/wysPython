# -*-coding:utf-8-*-
#==========================
#版本：0.1
#声明:本程序只用于学习交流，其他用途盖不负责
#time:2017-08-16
#author:笑看红尘
#人生酷苦短，人要偷懒
#==========================


import json
import re
from bs4 import BeautifulSoup
import  time
import HTMLParser
import requests
import threading
import redis
import urllib,urllib2,cookielib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = {'User-Agent': user_agent,
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           'Cookie': 'cna=BQmvD4q+MToCAWoCqxKaxG8H; cnaui=902479228; sca=50638f24; cdpid=WvA21vdKTcsM; aimx=HPImELeUVAACAWoCqxLZJWA8_1500976114; tbsa=127d599d389e2abb10bda028_1500976292_11; cad=t4AzsOKZm6fF9GqYQ/6B44TfzCBdDFs403SGvWUV4A4=0001; cap=9f60; atpsida=ba4e7f39849a05c1105b098d_1501037696_3; aui=902479228'      }
# 取代理Ip服务器
rconnection_Proxy = redis.Redis(host='117.122.192.50', port=6479, db=0)
# 代理IP
redis_key_proxy = "proxy:iplist2"
city=['sh','bj','tj','gz','sz','cd','nb','xm','fz','wh','km',
      'nj','dg','jn','fs','zh','cs','st','hk','xa','nn','nc','dy','qz','zj','sjz']

def ip_proxy():
    # 随机取IP
    proxy1 = rconnection_Proxy.srandmember(redis_key_proxy)
    proxyjson = json.loads(proxy1)
    proxiip = proxyjson["ip"]
    ip_list={'http': 'http://' + proxiip}
    return ip_list

class Url58TC():
    url='http:%s.58.com/chaoyang/chuzu/pn%s/'
    url='http://bj.58.com/xuanwu/chuzu/?PGTID=0d3090a7-0047-46db-c841-0c75d76c8ab6&ClickID=2'
    #获取页面数和城区
    def url_page(self):
        pass
    #进入下一级页面找属性
    def spider_num(self):
        proxy=ip_proxy()
        proxy_handler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        opener.addheaders = [(headers)]
        req = urllib2.urlopen(self.url, timeout=5)
        print req.read()




if __name__=="__main__":
    TC=Url58TC()
    TC.url_all()


































