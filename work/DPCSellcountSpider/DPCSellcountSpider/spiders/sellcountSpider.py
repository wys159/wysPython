# -*- coding: UTF-8 -*-
# Created by dev on 16-5-20.
# pip install scrapy
# pip install scrapy-redis
# pip install redis

import re
import sys
import json
import time
import datetime
import logging
import redis
import HTMLParser
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from DPCSellcountSpider.items import SellCountItem
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')

rconnection = redis.Redis(host='117.122.192.50', port=6479, db=0)
# max error times
Errorcount = 2


class SellcountSpider(RedisSpider):
    reReplace = re.compile('<.*?>|&.*?;')
    h = HTMLParser.HTMLParser()
    cookie = 't=f1d06870685879a126f29aef70568571; cookie2=6f00a95927be6e9e5aea864ba5a014d2;'
    name = "sellCountSpider"  # DailySellCountSpider sellCountSpider
    redis_key = '%s:start_urls' % name
    redis_key_starturl = '%s:start_urls' % name
    start_urls = [
        # '{"Urls": "https://detail.tmall.com/item.htm?id=525125609473","Urlleibie": "冰柜","Urlweb": "TM","spbjpinpai": "云麦","spbjjixing": "M1501","pc": "2016-07-21"}'
    ]
    # cookies = {
    #     "_tb_token_": "rygfso9k2jRxd",
    #     "cookie2": "41d91d3cb86216317f3b6cf160b995f7",
    #     "t": "0e7567fede0eef75c480a26da4f4f3e8",
    # }

    def make_requests_from_url(self, url):
        try:
            taskInfo = json.loads(url)
            spurl = str(taskInfo['Urls']).replace('http:', 'https:')
            print spurl
            if 'detail.tmall.com' in spurl:
                headers = {
                    "Accept": "*/*",
                    "Referer": "https://www.tmall.com/",
                    "Cookie": self.cookie
                }
                return Request(spurl, callback=self.parseTM, headers=headers, meta={'taskInfo': taskInfo},
                               dont_filter=True)
            else:
                print '*1' * 30
                self.log("error_URL:" + str(url), level=logging.ERROR)
        except Exception, ex:
            print 'make_requests_from_url error:', ex
            self.log("make_requests_from_url error:" + str(ex), level=logging.ERROR)

    # 天猫商城
    def parseTM(self, response):
        print '1' * 10
        taskInfo = response.meta['taskInfo']
        spurl = taskInfo['Urls']
        urlweb = taskInfo['Urlweb']
        pc = taskInfo.get('pc', '')
        spname = ''
        spleibie = taskInfo['Urlleibie']
        sppinpai = taskInfo['spbjpinpai']
        spxinghao = taskInfo['spbjjixing']
        webprice = ''
        spcuxiao = ''
        shopname = ''
        xiaoshoutype = ''
        item = SellCountItem()
        try:
            html = str(response.body).decode('gbk').encode('utf8')
            if '亲，访问受限了' in html or '小二在紧急处理，稍后再来哦' in html or '<div id="J_Static" class="static">' in html:
                print 'IP被封1-------------------------%s'
                headers = {
                    "Accept": "*/*",
                    "Referer": "https://www.tmall.com/",
                    # "Cookie": self.cookie
                }
                yield Request(spurl, callback=self.parseTM, headers=headers, meta={'taskInfo': taskInfo},
                              dont_filter=True)
            elif "很抱歉，您查看的商品找不到了" in html or "已下架" in html:
                item['spurl'] = spurl
                item['urlweb'] = urlweb
                item['pc'] = pc
                item['spname'] = "无效url"
                item['spleibie'] = spleibie
                item['sppinpai'] = ""
                item['spxinghao'] = ""
                item['webprice'] = ""
                item['spcuxiao'] = ""
                item['shopname'] = ""
                item['xiaoshoutype'] = ""
                yield Request(spurl, callback=self.parsePriceinfoTM, cookies=self.cookie, dont_filter=True,
                              # meta={'spurl': spurl, 'priceUrl': spurl, 'item': item})
                              meta={'spurl': spurl, 'priceUrl': spurl, 'item': item, 'errorcount': 0,
                                    'taskInfo': taskInfo})
            else:
                spnameReg = re.search('<input type="hidden" name="title" value="(?P<dd>[^<]*?)"', html)
                if spnameReg:
                    spname = spnameReg.group('dd')
                else:
                    spnameReg = re.search('title":"(?P<dd>.*?)"', html)
                    if spnameReg:
                        spname = spnameReg.group('dd')
                    else:
                        spnameReg = re.search('<h\d+ data-spm="\d+">(?P<dd>[\s\S]*?)</h', html)
                        if spnameReg:
                            spname = spnameReg.group('dd')

                spname = spname.replace('\r', '').replace('\n', '').replace('\t', '')
                if spname != '':
                    spname = re.sub(self.reReplace, '', spname)
                    if 'tm-yushou-process-banner' in html:
                        xiaoshoutype = '预售'

                    webPriceReg = re.search('defaultItemPrice":"(?P<dd>.*?)"', html)
                    if webPriceReg:
                        webprice = webPriceReg.group('dd')
                        if '-' in webprice:
                            webprice = webprice[0:webprice.find('-')].rstrip()

                    sppinpaiReg = re.search('brand":"(?P<dd>.*?)"', html)
                    if sppinpaiReg:
                        sppinpai = sppinpaiReg.group('dd')
                    spxinghaoReg = re.search('型号[^"]{0,5}:&nbsp;(?P<dd>.*?)</li>', html)
                    if spxinghaoReg:
                        spxinghao = spxinghaoReg.group('dd')
                    else:
                        spxinghaoReg = re.search('货号[^"]{0,5}:&nbsp;(?P<dd>.*?)</li>', html)
                        if spxinghaoReg:
                            spxinghao = spxinghaoReg.group('dd')

                    spcuxiaoReg = re.findall(
                        '</h.*?>\s+(<h4 class="tb-detail-sellpoint">(?P<cuxiao1>[\w\W]{0,100}?)?</h4>)?\s+<p>\s+(?P<cuxiao2>[\w\W]{0,100}?)?\s+</p>',
                        html)
                    if spcuxiaoReg:
                        for spcuxiaoS in spcuxiaoReg:
                            spcuxiao += re.sub(self.reReplace, '', ' '.join(spcuxiaoS))
                        spcuxiao = spcuxiao.lstrip().rstrip()
                    shopReg = re.search('seller_nickname" value="(?P<dd>.*?)"', html)
                    if shopReg:
                        shopname = shopReg.group('dd')
                    else:
                        shopReg = re.search('<a class="slogo-shopname" href=".*?">(?P<dd>.*?)</a>', html)
                        if shopReg:
                            shopname = shopReg.group('dd')
                        shopname = re.sub(self.reReplace, '', shopname)
                    priceUrl = re.search('"initApi"\s*?:\s*?"(?P<dd>[^"]*?)",', response.body).group('dd')
                    if 'https:' not in priceUrl:
                        priceUrl = 'https:' + priceUrl + '&callback=setMdskip&timestamp=' + str(int(time.time() * 1000))
                        # print priceUrl
                    headers = {
                        "Accept": "*/*",
                        "Referer": spurl,
                        # "Cookie": self.cookie
                    }
                    item['spurl'] = spurl
                    item['urlweb'] = urlweb
                    item['pc'] = pc
                    item['spname'] = spname
                    item['spleibie'] = spleibie
                    item['sppinpai'] = self.h.unescape(sppinpai)
                    item['spxinghao'] = self.h.unescape(spxinghao)
                    item['webprice'] = webprice
                    item['spcuxiao'] = spcuxiao
                    item['shopname'] = shopname
                    item['xiaoshoutype'] = xiaoshoutype
                    yield Request(priceUrl, callback=self.parsePriceinfoTM, headers=headers, dont_filter=True,
                                  meta={'spurl': spurl, 'priceUrl': priceUrl, 'item': item, 'errorcount': 0,
                                        'taskInfo': taskInfo})
        except Exception, ex:
            print 'parseTM error:', ex
            rconnection.rpush(self.redis_key_starturl, json.dumps(taskInfo))
            print "返回---return"
            return
            self.log("parseTM error:" + str(ex), level=logging.ERROR)

    def parsePriceinfoTM(self, response):
            try:
                print '2' * 10
                taskInfo = response.meta["taskInfo"]
                spurl = response.meta['spurl']
                priceUrl = response.meta['priceUrl']
                iteminfo = response.meta['item']
                errorcount = response.meta['errorcount']
                cxprice = ''
                sellcount = '0'
                quantity = '0'
                if 'window.location.href=' in str(response.body):
                    print 'IP被封122222------------------------------'
                    if errorcount == Errorcount:
                        rconnection.rpush(self.redis_key_starturl, json.dumps(taskInfo))
                        print "返回---return"
                        return
                    errorcount += 1
                    headers = {
                        "Accept": "*/*",
                        "Referer": spurl,
                        # "Cookie": self.cookie
                    }
                    yield Request(priceUrl, callback=self.parsePriceinfoTM, headers=headers, dont_filter=True,
                                  meta={'spurl': spurl, 'priceUrl': priceUrl, 'item': iteminfo,'errorcount': errorcount, 'taskInfo': taskInfo})
                elif ("很抱歉，您查看的商品找不到了" in str(response.body).decode('gbk').encode('utf8')) or ("已下架" in str(
                        response.body).decode('gbk').encode('utf8')):
                    item = SellCountItem()
                    item['spurl'] = spurl
                    item['urlweb'] = iteminfo['urlweb']
                    item['pc'] = iteminfo['pc']
                    item['spname'] = iteminfo['spname']
                    item['spleibie'] = iteminfo['spleibie']
                    item['sppinpai'] = iteminfo['sppinpai']
                    item['spxinghao'] = iteminfo['spxinghao']
                    item['webprice'] = iteminfo['webprice']
                    item['shopname'] = iteminfo['shopname']
                    item['cxprice'] = cxprice
                    item['spcuxiao'] = iteminfo['spcuxiao']
                    item['skuid'] = ""
                    item['spplriqi'] = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
                    item['quantity'] = quantity
                    item['sellcount'] = sellcount
                    item['xiaoshoutype'] = iteminfo['xiaoshoutype']
                    item['collectiontime'] = str(datetime.datetime.now())
                    print "result success : invalid url"
                    yield item
                else:
                    print "ht,ddddddd"
                    html = str(response.body).decode('gbk').encode('utf8')
                    try:
                        sellcountReg = re.search('sellCount":(?P<dd>\d+)', html)
                        if sellcountReg:
                            sellcount = str(sellcountReg.group('dd'))
                            if sellcount == '' or sellcount.lower() == 'null' or sellcount == 'None':
                                sellcount = '0'
                        spjgMTempReg = re.search('priceInfo":{(?P<dd>.*?)}},', html)
                        if spjgMTempReg:
                            spjgMTemp = spjgMTempReg.group('dd')
                            skuSReg = re.findall('"(?P<dd>[^"]*?)":{', spjgMTemp)
                            if len(skuSReg) > 0:
                                for skuid in skuSReg:
                                    item = SellCountItem()
                                    try:
                                        if re.match('\d+$', str(skuid)):
                                            quantityReg = re.search('"%s":{"quantity":(?P<dd>\d+)' % str(skuid), html)
                                            if quantityReg:
                                                quantity = quantityReg.group('dd')
                                            regStr = re.compile(
                                                '"%s"[^}]*?promotionList[^}]*?"price":"(?P<dd>\d+\.\d+)"' % str(skuid))
                                            if 'promotionList' not in html:
                                                regStr = re.compile(
                                                    '"%s":{"areaSold":true.*?"price":"(?P<dd>\d+\.\d+)"' % str(skuid))
                                            cxPriceReg = re.search(regStr, html)
                                            if cxPriceReg:
                                                cxprice = cxPriceReg.group('dd')
                                        else:
                                            quantity = '0'
                                            priceM = re.search('"priceInfo"[\s\S]*?}}', html).group()
                                            spjgS = re.findall('"price":"(?P<dd>.*?)"', priceM)
                                            if len(spjgS) > 0:
                                                cxprice = str(spjgS[0])
                                                for i in range(len(spjgS)):
                                                    try:
                                                        if float(cxprice) > float(str(spjgS[i])) and float(
                                                                str(spjgS[i])) > 0:
                                                            cxprice = str(spjgS[i])
                                                    except:
                                                        pass
                                        if cxprice == '':
                                            cxprice = iteminfo['webprice']
                                    except:
                                        pass
                                    item['spurl'] = spurl
                                    item['urlweb'] = iteminfo['urlweb']
                                    item['pc'] = iteminfo['pc']
                                    item['spname'] = iteminfo['spname']
                                    item['spleibie'] = iteminfo['spleibie']
                                    item['sppinpai'] = iteminfo['sppinpai']
                                    item['spxinghao'] = iteminfo['spxinghao']
                                    item['webprice'] = iteminfo['webprice']
                                    item['shopname'] = iteminfo['shopname']
                                    item['shopname'] = iteminfo['shopname']
                                    item['cxprice'] = cxprice
                                    item['spcuxiao'] = iteminfo['spcuxiao']
                                    item['skuid'] = skuid
                                    item['spplriqi'] = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
                                    item['quantity'] = quantity
                                    item['sellcount'] = sellcount
                                    item['xiaoshoutype'] = iteminfo['xiaoshoutype']
                                    item['collectiontime'] = str(datetime.datetime.now())
                                    print "result success"
                                    yield item

                    except Exception, ex:
                        print "12x1"
                        self.log("parsePriceinfoTM error:" + str(ex), level=logging.ERROR)
            except Exception, exx:
                print traceback.format_exc()
                print 'parsePriceinfoTM2 error:', exx
                self.log("parsePriceinfoTM2 error:" + str(exx), level=logging.ERROR)