# -*- coding: UTF-8 -*-
# Created by dev on 16-1-25.
import logging
import datetime
import time
import json
import  re
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from DPC_Spider_JDYuShou.items import JDYushou
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class EcSpider(RedisSpider):
    name = "DPC_Spider_JDYuShou"
    redis_key = '%s:start_urls_info' % name
# name = "SqlServerInsertAllUrl2"
# redis_key = 'SqlServerInsertAllUrl2:start_urls_info'

# start_urls = {'{ "url":"https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.jMG3s1&id=539421106833&skuId=3262730024459&standard=1&user_id=197232874&cat_id=50024400&is_b=1&rn=fffff6ed5cda7c76029d5dcf5c1f0b66","attr":{"urlweb":"urlweb","brand":"brand","urlleibie":"urlleibie","model":"model"}}',
#    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    }
    headers_1 = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Host": "mdskip.taobao.com",
        "Referer": "https://detail.tmall.com/item.htm?id=521212323526",
    }


    def make_requests_from_url(self, redis_data):
        data = json.loads(redis_data)
        url = data['Urls']
        attr_data = {'Urlleibie':data['Urlleibie'],'Urlweb':data['Urlweb'],'spbjpinpai':data['spbjpinpai'],'spbjjixing':data['spbjjixing']}
        canshu_data = {"attr": attr_data, "sp_url": url}
        print '*' * 100
        print "Spider_start_Url:" + str(url)
        if 'item.jd.com' in str(url):
            return Request(url, callback=self.parseJD, dont_filter=True, meta=canshu_data)
        else:
            with open('error_url', 'a+') as f:
                f.write(str(url) + '\n')
    def parseJD(self,response):
        sxurl=response.meta['sp_url']
        sx_attr=response.meta['attr']
        spurl = response.url
        # if 'https://www.jd.com/?d' in spurl:

        # 获取页数
        try:
            html = response.body
            mm = response.encoding
            if 'GB18030' in mm or 'gb18030' in mm:
                html = html.decode('GB18030')
            elif ('gb' in str(mm) or 'GB' in str(mm) ):
                html = html.decode('GBK')
            if '<!--yushou-->' in html:
                #商品名称
                spname = response.xpath('//*[@id="name"]/h1/text()|//div[@class="sku-name"]/text()').extract()
                print spname
                productid = re.search('\d+', spurl).group()  # url id
                print productid
                plheaders = {"Referer": "" + spurl + ""}
                yushouproductid='https://yushou.jd.com/youshouinfo.action?callback=fetchJSON&sku=%s'%productid
                yield Request(yushouproductid, callback=self.parseJDYushou, headers=plheaders,dont_filter=True,
                               meta={'url':sxurl,'skuid':productid,'spname':spname[0],'attr':sx_attr})
            else:
                print  '当前页面：%s 不是预售'%sxurl

        except Exception,e:
            print "进入详情出错：%s"%e
    def parseJDYushou(self,response):
        item = JDYushou()
        try:
            spurl=response.url
            html = response.body
            plheaders = {"Referer": "" + spurl + ""}
            productid=response.meta['skuid']
            mm = response.encoding
            if 'GB18030' in mm or 'gb18030' in mm:
                html = html.decode('GB18030')
            elif ('gb' in str(mm) or 'GB' in str(mm)):
                html = html.decode('GBK')
            htmljson=html.replace('fetchJSON(','')
            htmljs=htmljson[:-2]
            htmljs=json.loads(htmljs)
            if htmljs['type']=='1':
                yuyuepersonNum=htmljs['num']
            #采集预售中的品牌，型号，url,电商,预约人,品类
            item['spurl']=response.meta['url']
            item['spname']=response.meta['spname']
            item['spxinghao']=response.meta['attr']['spbjjixing']
            item['sppinpai'] = response.meta['attr']['spbjpinpai']
            item['urlweb']= response.meta['attr']['Urlweb']
            item['spleibie'] = response.meta['attr']['Urlleibie']
            item['sellcount']=yuyuepersonNum

            item['spcuxiao'] = ''
            item['cxprice'] = ''
            item['shopname'] =''
            item['collectiontime'] = ''
            item['pc'] = ''
            item['spplriqi'] = ''
            item['webprice'] = ''
            item['skuid'] = ''
            item['xiaoshoutype'] = ''
            item['quantity'] = ''

            yield  item
        except Exception,e:
            print "进入第一种预约页面有可能不对，正在进入下一种页面......：%s" % e
            # 'https://yuding.jd.com/presaleInfo/getPresaleInfo.action?callback=jQuery&sku=1561087004&_=%s' % str(
            #     int(time * 1000))
            t=str(int(time.time()*1000))

            yushouproductid = 'https://yuding.jd.com/presaleInfo/getPresaleInfo.action?callback=jQuery&sku=%s&_=%s'%(productid,t)
            yield Request(yushouproductid, callback=self.parseJDYushouType, headers=plheaders, dont_filter=True,
                          meta={'url': response.meta['url'], 'skuid': productid, 'spname': response.meta['spname'],
                                'attr': response.meta['attr']})

    def parseJDYushouType(self,response):
        item = JDYushou()
        try:
            spurl = response.url
            html = response.body
            # plheaders = {"Referer": "" + spurl + ""}
            # productid = response.meta['skuid']
            mm = response.encoding
            if 'GB18030' in mm or 'gb18030' in mm:
                html = html.decode('GB18030')
            elif ('gb' in str(mm) or 'GB' in str(mm)):
                html = html.decode('GBK')
            htmljson = html.replace('jQuery(', '')
            htmljs = htmljson[:-1]
            htmljs = json.loads(htmljs)
            if htmljs['type'] == '2':
                yuyuepersonNum = htmljs['ret']['count']

            # 采集预售中的品牌，型号，url,电商,预约人,品类
            item['spurl'] = response.meta['url']
            item['spname'] = response.meta['spname']
            item['spxinghao'] = response.meta['attr']['spbjjixing']
            item['sppinpai'] = response.meta['attr']['spbjpinpai']
            item['urlweb'] = response.meta['attr']['Urlweb']
            item['spleibie'] = response.meta['attr']['Urlleibie']
            item['sellcount'] = yuyuepersonNum

            item['spcuxiao'] = ''
            item['cxprice'] = ''
            item['shopname'] = ''
            item['collectiontime'] = ''
            item['pc'] = ''
            item['spplriqi'] = ''
            item['webprice'] = ''
            item['skuid'] = ''
            item['xiaoshoutype'] = ''
            item['quantity'] = ''

            yield item
        except Exception, e:
            print "进入第二种页面预约出错：%s" % e






