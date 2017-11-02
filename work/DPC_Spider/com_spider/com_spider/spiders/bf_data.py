#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import redis
import json
import re
import datetime
import MySQLdb
import urllib,urllib2
import requests
import traceback
import time
import xconfig
import random
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
REDIS_HOST = settings.get('REDIS_HOST')
REDIS_PORT = settings.get('REDIS_PORT')
IP_USER = settings.get('IP_USER')
IP_PWD = settings.get('IP_PWD')


def bf_submit(redisname,data,key,strtime):
    if redisname == "comment_spider":
        redisname = "SqlServerInsertAllUrl"
    else:
        redisname = "SqlServerInsertAllUrl2"
    if key =="result_items":
        # data['crawltime'] = strtime
        submitdata = json.dumps(data)
        rds = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        rds.lpush("%s:items"%(str(redisname)),submitdata)
    elif key == "no_comment":
        data['crawltime'] = strtime
        submitdata = json.dumps(data)
        rds = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        rds.lpush("%s:no_comment"%(str(redisname)),submitdata)
    elif key == "bf_url":
        data['crawltime'] = strtime
        submitdata = json.dumps(data)
        rds = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        rds.lpush("%s:bf_url"%(str(redisname)),submitdata)
    else:
        print u'key值传入错误'


def shop_name_suning(id):
    try:
        canshu1 = "http://icps.suning.com/icps-web/getAllPriceFourPage/000000000"
        canshu2 = "__010_0100101_1_pc_showSaleStatus.vhtm"
        url = canshu1 + str(id) + canshu2
        htmlpage = urllib2.urlopen(url, timeout=20).read()
        if 'vendor' in str(htmlpage):
            vendor = re.findall('"vendor":"(.*?)"',htmlpage)
            vendorid = vendor[0].strip() if vendor else ""
        else:
            vendorid = ""
        if vendorid:
            canshu3 = "http://product.suning.com/pds-web/ajax/getVendorListInfo_"
            shopnameurl = canshu3 + str(vendorid)+".html"
            shophtmlpage = urllib2.urlopen(shopnameurl, timeout=10).read()
            print shophtmlpage
            nameget = re.findall('"shopName":"(.*?)"', shophtmlpage)
            name = nameget[0].strip() if nameget else ""
            return name
        else:
            name = ""
            return name
    except Exception,e:
        print u'shopname ----------error'
        print e
        name = ""
        return name


def mysql_submit(data,key):
    try:
        print '*' * 30
        return 1
        # if key:
        #     mdb[key].insert(data)
        #     return 1
        # else:
        #     print u'mongo数据库入库时 KEY 错误'
        #     return 2
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
        return 2


def replies_suning(url):
    try:
        # r = requests.get(url)
        # data =  str(r.text)
        r = urllib2.urlopen(url, timeout=10)
        data = r.read()
        return data
    except Exception, e:
        print e
        return u'无回复数据'


def shixiaourl(url, attr):
    rds = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    sx_data ={'url':url,'attr':attr}
    submit_data = json.dumps(sx_data)
    rds.lpush("comment_spider:sx_url",submit_data)
    # rds.lpush("comment_bf_data:sx_url",submit_data)
    key='spider_error'
    mysql_submit(data=sx_data, key=key)


def yhd_page(url,pid, pagenumber):
    settings = get_project_settings()
    proxykeys = settings.get("PROXYKEYS")
    try:
       plheaders = {
                "Accept":"*/*",
                "Connection":"keep-alive",
                "Cookie":xconfig.YHD_COOKIE,
                "Host":"e.yhd.com",
                "Referer":url,
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
            }
       url_param_1 = "http://e.yhd.com/front-pe/productExperience/proExperienceAction!ajaxView_pe.do?product.id="
       product_id = pid
       url_param_2 = "&merchantId=201045&filter.orderType=newest&pagenationVO.currentPage="
       pagenumber = pagenumber
       url_param_3 = "&pagenationVO.preCurrentPage="+str(int(pagenumber)-1)+"&pagenationVO.rownumperpage=5&currSiteId=1&currSiteType=2&filter.commentFlag=total&filter.sortFlag=order_by_createtime&tt=Wed%20Nov%2002%202016%2011:35:05%20GMT+0800&filter.mainProdId=null&filter.labelId=null&peCode=-1&_=1478057497522"
       spurl = url_param_1 + str(pid) + url_param_2 + str(pagenumber) + url_param_3
       redisclient = redis.Redis(host=xconfig.REDIS_HOST, port=xconfig.REDIS_PORT)
       proxy = redisclient.srandmember(random.choice(proxykeys))
       proxyjson = json.loads(proxy)
       ip = proxyjson["ip"]
       proxy_handler = urllib2.ProxyHandler({"http": "http://" + IP_USER + ":" + IP_PWD + "@%s" % ip})
       opener = urllib2.build_opener(proxy_handler)
       urllib2.install_opener(opener)
       req = urllib2.Request(spurl, headers=plheaders)
       res = urllib2.urlopen(req, timeout=10)
       htmlpage = res.read()
       if htmlpage:
           return htmlpage
       else:
           print u'一号店获取评论源码失败'
           return {}
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg

if __name__ == "__main__":
    data = {'attr': {u'brand': u'brand',
          u'model': u'model',
          u'urlleibie': u'urlleibie',
          u'urlweb': u'urlweb',
          u'xxxx': u'xxxx'},
 'color': u'\u9ed1\u8272',
 'cx_info': '\xe3\x80\x90\xe4\xb8\x8b\xe5\x8d\x95\xe7\xab\x8b\xe5\x87\x8f100!2999\xe6\x88\x90\xe4\xba\xa4\xe3\x80\x91\xe3\x80\x90\xe7\xbe\x8e\xe7\x9a\x84\xe2\x80\x9c\xe6\x99\xba\xe5\x9c\xa8\xe5\xbf\x85\xe5\xbe\x97\xe2\x80\x9d\xe6\x96\xb0\xe5\x93\x81\xe5\x8f\x91\xe5\xb8\x83\xe4\xbc\x9a\xe5\x8a\x9b\xe8\x8d\x90\xe4\xba\xa7\xe5\x93\x81\xe3\x80\x91\xe5\xa4\x9a\xe5\x8a\x9f\xe8\x83\xbd\xe9\x99\xa4\xe8\x8f\x8c\xe6\xb4\x97\xe7\xa2\x97\xe6\x9c\xba,\xe9\x99\xa4\xe8\x8f\x8c\xe7\x8e\x8799.99%:\xe6\xb4\x97\xe7\xa2\x97+\xe9\x99\xa4\xe8\x8f\x8c+\xe5\x82\xa8\xe8\x97\x8f=\xe9\x94\x85\xe7\xa2\x97\xe7\x93\xa2\xe7\x9b\x86\xe4\xb8\x80\xe9\x83\xa8\xe6\x90\x9e\xe5\xae\x9a.8\xe5\xa5\x97\xe5\xae\xb9\xe9\x87\x8f,\xe4\xb8\xad\xe5\xbc\x8f\xe7\xa2\x97\xe7\xaf\xae!8L\xe6\xb0\xb4\xe6\xa0\x87\xe5\x87\x86\xe6\xb4\x97!\xe9\xab\x98\xe6\xb8\xa9\xe9\xab\x98\xe5\x8e\x8b\xe6\xb0\xb4360\xc2\xb0\xe5\x86\xb2\xe6\xb4\x97,\xe6\xb4\x81\xe5\x87\x80\xe4\xb8\x8d\xe7\x95\x99\xe7\x97\x95!',
 'productColor': '',
 'replies': '',
 'sp_brand': u'\u7f8e\u7684',
 'sp_dianp': u'\u7f8e\u7684\u53a8\u7535\u65d7\u8230\u5e97',
 'sp_maijia': u'j***1',
 'sp_models': 'WQP8-3905-CN',
 'sp_name': u'\u7f8e\u7684\uff08Midea\uff098\u5957 \u5168\u81ea\u52a8\u5bb6\u7528 \u9ad8\u6e29\u9664\u83cc\u5d4c\u5165\u5f0f\u6d17\u7897\u673a WQP8-3905-CN',
 'sp_pl': u'\u5f88\u597d\u7528\uff0c\u89e3\u51b3\u4e86\u53cc\u624b\uff0c\u6d17\u7684\u5e72\u51c0\uff0c\u9ad8\u6548',
 'sp_plriqi': u'2016-12-04 21:42:32',
 'sp_score': 5,
 'sp_url': u'https://item.jd.com/1300999.html',
 'sp_web_price': u'2999.00'}
    print mysql_submit(data=data,key='result_items')
