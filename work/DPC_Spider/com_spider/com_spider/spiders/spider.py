# -*- coding: UTF-8 -*-
# Created by dev on 16-1-25.
import logging
import datetime
from bf_data import bf_submit,shop_name_suning,mysql_submit,replies_suning,shixiaourl
from bf_data import yhd_page
from base_info import *
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from com_spider.items import AvccollectionagentItem
reload(sys)
sys.setdefaultencoding('utf-8')

import redis

settings = get_project_settings()
REDIS_HOST = settings.get('REDIS_HOST')
REDIS_PORT = settings.get('REDIS_PORT')
IP_USER = settings.get('IP_USER')
IP_PWD = settings.get('IP_PWD')
PROXYKEYS = settings.get('PROXYKEYS')
rconnection_yz = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


class EcSpider(RedisSpider):
    name = "comment_spider"
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
        url = data['url']
        attr_data = data['attr']
        canshu_data = {"attr":attr_data,"sp_url":url}
        print "Spider_start_Url:" + str(url)
        if 'detail.tmall.com' in str(url):
            return Request(url, callback=self.parseTM, headers=self.headers, dont_filter=True, meta=canshu_data)
        elif 'item.jd.com' in str(url):
            return Request(url, callback=self.parseJD, dont_filter=True, meta=canshu_data)
        elif 'product.suning.com' in str(url):
            return Request(url, callback=self.parseSN, dont_filter=True,meta=canshu_data)
        elif 'gome.com.cn' in str(url):
            print '*'*100
            return Request(url, callback=self.parseGM, dont_filter=True, meta=canshu_data)
        elif 'item.yixun.com' in str(url):
            return Request(url, callback=self.parseYX, dont_filter=True, meta=canshu_data)
        elif 'item.yhd.com' in str(url):
            print '*' * 100
            return Request(url, callback=self.parseYHD, dont_filter=True, meta=canshu_data)
        elif 'www.amazon.cn' in str(url):
            return Request(url, callback=self.parseYMX, dont_filter=True, meta=canshu_data)
        elif 'product.dangdang.com' in str(url):
            return Request(url, callback=self.parseDD, dont_filter=True, meta=canshu_data)
        else:
            with open('error_url','a+') as f:
                f.write(str(url)+'\n')

    # 天猫商城
    def parseTM(self, response):
        sxurl = response.meta['sp_url']
        sx_attr=response.meta['attr']
        if u'您查看的商品找不到了'.encode("gbk") in response.body:shixiaourl(url=sxurl,attr=sx_attr)
        try:
            spurl = response.url
            spname = response.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/a/text()').extract()
            spname_1 = response.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/text()').extract()
            if len(spname)>=1 :
                spname = spname[0].strip() if spname else ""
            else:
                spname = spname_1[0].strip() if spname_1 else ""
            itemId = re.search('"itemId":"(?P<dd>\d+)"', str(response.body)).group('dd')
            spuId = re.search('"spuId":"(?P<dd>\d+)"', str(response.body)).group('dd')
            sellerId = re.search('"sellerId":(?P<dd>\d+)', str(response.body)).group('dd')
            spplurltemp = ('https://rate.tmall.com/list_detail_rate.htm?itemId=_itemId_&spuId=_spuId_'
                           '&sellerId=_sellerId_&order=1&currentPage=_p_&append=0&content=1&tagId=&posi=&picture=')
            plheaders = {"Referer": "" + spurl + ""}
            item = AvccollectionagentItem()
            sp_dianp = response.xpath('//a[@class="slogo-shopname"]/strong/text()').extract()
            item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp[0] else ""
            item['attr'] = response.meta['attr']
            item['sp_url'] = response.meta['sp_url']
            item['sp_name'] = spname
            skuId = re.findall('"skuId":(.*?)}', response.body)
            if skuId :
                skuId = skuId[0].strip()
            else:
                skuId = re.search('\d+',(response.url).split('&')[-1].strip())
                skuId = skuId.group() if skuId else ""
            spplurl = spplurltemp.replace('_itemId_',
                                          itemId).replace('_spuId_',
                                                          spuId).replace('_sellerId_', sellerId).replace('_p_', '1')
            spplurl = spplurl + '&needFold=0'
            attr = response.meta['attr']
            ip = response.meta['proxy']
            item['sp_brand'] = item['sp_models'] = item['color'] = item['sp_web_price'] = item['cx_info']=""
            yield Request(spplurl, callback=self.parseContentTM, headers=plheaders, dont_filter=True,
                          meta={'item': item, 'spplurltemp': spplurltemp, 'itemId': itemId, 'spuId': spuId,
                                'sellerId': sellerId, 'pagenum': '1','id':{"pid":0,"uid":0},'starturl':response.url,
                                'spplurl':"",'attr':attr,
                                })
        except:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url
            attr = response.meta['attr']
            strtime = str(datetime.datetime.now())
            attr['url'] = response.url
            attr['crawltime']= strtime
            data = attr
            key = "bf_url"
            print u'被封数据已经保存到数据库--------天猫'
            k = mysql_submit(data=data,key=key)
            print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'

    def parseContentTM(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        itemId = response.meta['itemId']
        spuId = response.meta['spuId']
        sellerId = response.meta['sellerId']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        pid = response.meta['id']['pid']
        starturl = response.meta['starturl']
        pageurl = response.meta['spplurl']
        attr = response.meta['attr']
        nocomment=[]
        try:
            htmlsource = str(response.body).decode('gbk').encode('utf8')
            pljsons = str(htmlsource).split('<!doctype html>')[0].replace('"rateDetail":','',1).strip()
            print u'源码以保存'
            pljson = json.loads(pljsons)
            pljson = pljson['rateDetail']['rateList'] if 'rateDetail' in str(pljson.keys()) else pljson['rateList']
            for pljsoninfo in pljson:
                    iteminfo = AvccollectionagentItem()
                    try:
                        iteminfo['sp_url'] = item['sp_url']
                        iteminfo['sp_name'] = item['sp_name']
                        iteminfo['sp_maijia'] = pljsoninfo['displayUserNick']
                        serviceRateContent = pljsoninfo['serviceRateContent']
                        sp_pl = str(pljsoninfo['rateContent']) + "。" + serviceRateContent
                        iteminfo['sp_pl'] = re.sub(r'<[^>]+>','',sp_pl) if sp_pl else ""
                        iteminfo['sp_plriqi'] = pljsoninfo['rateDate']
                        iteminfo['sp_dianp']  = item['sp_dianp']
                        iteminfo['attr'] = item['attr']
                        iteminfo['sp_score'] = ""
                        iteminfo['productColor'] = pljsoninfo['auctionSku']
                        iteminfo['sp_brand'] = item['sp_brand']
                        iteminfo['sp_models'] = item['sp_models']
                        iteminfo['color'] = item['color']
                        iteminfo['sp_web_price'] = item['sp_web_price']
                        iteminfo['cx_info'] = item['cx_info']
                        # add 回复：
                        if pljsoninfo['reply']:
                            replieslist = list()
                            repliesdict = dict()
                            repliesdict['sp_name'] = u'官方客服'
                            repliesdict['sp_plriqi'] = iteminfo['sp_plriqi']
                            repliesdict['sp_pl'] = pljsoninfo['reply']
                            repliesdict['official_reply'] = 1
                            replieslist.append(repliesdict)
                            iteminfo['replies'] =replieslist
                        else:
                            iteminfo['replies'] = ""
                    except Exception, ex:
                        error_msg = traceback.format_exc()
                        attr = response.meta['attr']
                        strtime = str(datetime.datetime.now())
                        attr['url'] = starturl
                        attr['crawltime']= strtime
                        data = attr
                        key = "bf_url"
                        print u'被封数据已经保存到数据库--------天猫'
                        print data
                        k = mysql_submit(data=data,key=key)
                        print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'
                    if str(iteminfo['sp_plriqi']) > old_time:
                    # if 1:
                        pid = pid + 1
                        nocomment.append(str(iteminfo['sp_plriqi']))
                        data = dict(iteminfo)
                        key = "result_items"
                        strtime = str(datetime.datetime.now())
                        print data
                        bf_submit(redisname=self.name, data=data, key=key, strtime=strtime)
                        print u'数据已经备份'
                        k = mysql_submit(data=data, key=key)
                        print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'
                        yield iteminfo
                    else:
                        pass
            if not nocomment and int(pid)==0:
                attr["url"]= starturl
                data = attr
                key = "no_comment"
                # strtime = str(datetime.datetime.now()).split(' ')[0].strip()
                strtime = str(datetime.datetime.now())
                #　bf_submit('comment_bf_data',data=data,key=key,strtime=strtime)
                print u'无评论数据已上传'
                k = mysql_submit(data=data,key=key)
                print u'无评论数据已保存到数据库' if k==1 else  u'数据入库出现问题'
                # break
            else:
                pass

            if str(iteminfo['sp_plriqi']) > old_time:
            # if 1:
                    plheaders = {"Referer": "" + item['sp_url'] + ""}
                    spplurl = spplurltemp.replace('_itemId_',
                                                  itemId).replace('_spuId_',
                                                                  spuId).replace('_sellerId_',
                                                                                 sellerId).replace('_p_', pagenum)
                    spplurl = spplurl + '&needFold=0'
                    time.sleep(2)
                    print spplurl
                    yield Request(spplurl, callback=self.parseContentTM, headers=plheaders, dont_filter=True,
                                  meta={'item': item, 'spplurltemp': spplurltemp, 'itemId': itemId, 'spuId': spuId,
                                        'sellerId': sellerId, 'pagenum': pagenum,'id':{"pid":pid},'starturl':starturl,
                                        'spplurl': spplurl,'attr': attr})
            else:
                print u'此页数据采集完成'
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print u'网站可能被封'
            print response.url
            print attr
            if pid < 2:
                spplurl = pageurl if pageurl else starturl
                time.sleep(2)
                plheaders = {"Referer": "" + item['sp_url'] + ""}
                pid = pid +1
                yield Request(spplurl, callback=self.parseContentTM, headers=plheaders, dont_filter=True,
                                  meta={'item': item, 'spplurltemp': spplurltemp, 'itemId': itemId, 'spuId': spuId,
                                        'sellerId': sellerId, 'pagenum': pagenum,'id':{"pid":pid},'starturl':starturl,'spplurl':spplurl,'attr':attr})
            else:
                print u'测试3次失败'
                attr["url"]= starturl
                data = attr
                key = "bf_url"
                strtime = str(datetime.datetime.now())
                k = mysql_submit(data=data,key=key)
                print u'被封url已保存到数据库' if k==1 else  u'数据入库出现问题'

    # 京东商城
    def parseJD(self, response):
        sxurl = response.meta['sp_url']
        sx_attr = response.meta['attr']
        if 'cdn4' in str(response.url):shixiaourl(url=sxurl, attr=sx_attr)
        try:
            item = AvccollectionagentItem()
            spurl = response.url
            spname = response.xpath('//*[@id="name"]/h1/text()|//div[@class="sku-name"]/text()').extract()  # 商品名称
            productid = re.search('\d+', spurl).group()     # url id
            plheaders = {"Referer": "" + spurl + ""}
            item['attr'] = response.meta['attr']
            item['sp_url'] = response.meta['sp_url']
            dianp = response.xpath('//div[@class="seller-infor"]/a//text()|\
                                   //div[@class="seller-infor"]/em/text()|\
                                   //div[@class="contact fr clearfix"]/div/div/a/text()').extract()  # 店铺
            if dianp:
                dianp = dianp
            else:
                dianp = response.xpath('//div[@class="popbox-inner"]/div/h3/a/text()').extract()
            item['sp_name'] = spname[0].strip() if spname else ""
            item['sp_dianp'] = dianp[0].strip() if dianp else ""
            # wgh 2017-9-8
            if len(item['sp_name']) == 0:
                spname = re.search('(?<=sku-name">)[\s\S]+?(?=</div>)', str(response.body).decode("gbk", "ignore"))
                if spname:
                    delete = re.search('<.*?>', spname.group()).group()
                    spname = spname.group().replace(delete, "").strip()
                    item['sp_name'] = spname
            # canshu1 = "http://club.jd.com/comment/getSkuProductPageComments.action?productId="
            # canshu1 = "http://club.jd.com/comment/productPageComments.action?productId="
            # canshu2 = "&score=0&sortType=3&page=0&pageSize=10"
            canshu1 = "https://club.jd.com/comment/skuProductPageComments.action?productId="  # wgh 2017-9-6
            # canshu2 = "&score=0&sortType=6&page=0&pageSize=10"  # sort type=6 按照时间排序
            canshu2 = "&score=0&sortType=6&page=0&pageSize=10"  # sort type=6 按照时间排序
            spplurl = canshu1 + productid + canshu2
            attr = response.meta['attr']
            starturl = response.meta['sp_url']
            phtml = str(response.body).strip()
            ip = response.meta['proxy']
            baseinfo = jd_base_info(spurl, ip)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            item['cx_info'] = baseinfo['cx_info']
            yield Request(spplurl, callback=self.parseContentJD, headers=plheaders, dont_filter=True,
                          meta={'item': item, 'spplurltemp': spplurl,'productid': productid, 'pagenum': '0',
                                'id':{"pid": 0, "uid": 0, "fid": 0},'starturl': starturl, 'attr': attr}
                          )
        except Exception, ex:
            print '2'* 10
            error_msg = traceback.format_exc()
            print error_msg
            attr = response.meta['attr']
            strtime = str(datetime.datetime.now())
            attr['url'] = response.url
            starturl=response.meta['sp_url']
            attr['crawltime']= strtime
            data = attr
            key = "bf_url"
            print data
            k = mysql_submit(data=data, key=key)
            print u'被封 数据 保存到数据库' if k==1 else  u'数据入库出现问题'

    def parseContentJD(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        # old_time = str(datetime.datetime.now() + datetime.timedelta(days=-40))[0:10]  # 截取标准日期格式:2017-010-02
        pid = response.meta['id']['pid']
        uid = response.meta['id']['uid']
        fid = response.meta['id']['fid']
        starturl = response.meta['starturl']
        attr = response.meta['attr']
        # thefirsttimes
        firsttimes = 0  # 判断第一次出现的评论的日期范围（7天）
        endtimes = 0   # 最后一次查询评论的日期范围（7天）
        nocomment=[]
        try:
            if not str(response.body).strip():
                if fid < 3:
                    fid = fid + 1
                    time.sleep(5)
                    plheaders = {"Referer": "" + item['sp_url'] + ""}
                    # canshu1 = "http://club.jd.com/comment/getSkuProductPageComments.action?productId="
                    # canshu1 = "http://club.jd.com/comment/productPageComments.action?productId="
                    # canshu2 = "&score=0&sortType=6&pageSize=10" # &page=0
                    canshu1 = "https://club.jd.com/comment/skuProductPageComments.action?productId="  # wgh 2017-9-6
                    canshu2 = "&score=0&sortType=6&pageSize=10"
                    spplurl = canshu1 + productid + canshu2 + "&page=" + str(pagenum)
                    yield Request(spplurl, callback=self.parseContentJD, headers=plheaders, dont_filter=True,
                                                  meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                                        'pagenum': pagenum,'id':{'pid':pid,'uid':uid,'fid':fid},'starturl':starturl,'attr':attr})
                else:
                    pass
            else:
                try:
                    # #将获取的字符串strTxt做decode时，指明ignore，会忽略非法字符
                    pljsons = json.loads(str(response.body).strip().decode('gbk', 'ignore').encode('utf-8'))
                    pljson = pljsons['comments']
                    if len(pljson) > 0:
                        for pljsoninfo in pljson:
                            iteminfo = AvccollectionagentItem()
                            try:
                                # 采集的产品id,是否和url 的id 一致
                                product_id = pljsoninfo["referenceId"]
                                iteminfo['sp_url'] = item['sp_url']
                                iteminfo['sp_name'] = item['sp_name']
                                iteminfo['sp_maijia'] = pljsoninfo['nickname']
                                iteminfo['sp_pl'] = pljsoninfo['content']
                                iteminfo['sp_plriqi'] = pljsoninfo['creationTime']
                                # add score ( 评论指数 )
                                iteminfo['sp_score'] = pljsoninfo['score']
                                iteminfo['sp_dianp'] = item['sp_dianp']
                                iteminfo['productColor'] = ""
                                iteminfo['attr'] = item['attr']
                                iteminfo['sp_brand'] = item['sp_brand']
                                iteminfo['sp_models'] = item['sp_models']
                                iteminfo['color'] = item['color']
                                iteminfo['sp_web_price'] = item['sp_web_price']
                                iteminfo['cx_info'] = item['cx_info']
                                # 增加回复
                                if "replies" in pljsoninfo.keys():
                                    rep_list = list()
                                    for rep in pljsoninfo['replies']:
                                        repdata = dict()
                                        if rep['userClient'] == 99:
                                            repdata['sp_pl'] = rep["content"].strip() if rep else ""
                                            repdata['sp_plriqi'] = rep['creationTime'] if rep else ""
                                            repdata['sp_name'] = rep['nickname'] if rep else ""
                                            repdata['official_reply'] = 1
                                            rep_list.append(repdata)
                                        else:
                                            repdata['official_reply'] = 0
                                    rep_list.append(repdata)
                                    iteminfo['replies'] = rep_list if rep_list else ""
                                else:
                                    iteminfo['replies'] = ""
                            except Exception, ex:
                                error_msg = traceback.format_exc()
                                print error_msg
                                print response.url
                            if str(iteminfo['sp_plriqi']) > old_time:
                                if productid == product_id:
                                    pid = 0
                                    uid = 1
                                    firsttimes = 1  # 第一次出现
                                    nocomment.append(str(iteminfo['sp_plriqi']))
                                    data = dict(iteminfo)
                                    key = "result_items"
                                    strtime = str(datetime.datetime.now())
                                    bf_submit(redisname=self.name, data=data, key=key, strtime=strtime)
                                    print json.dumps(dict(data), indent=1, ensure_ascii=False)
                                    k = mysql_submit(data=data, key=key)
                                    print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'*10
                                    yield iteminfo
                                else:
                                    print "product id  not real"
                            else:
                                pid += 1
                                if firsttimes == 1:
                                    firsttimes = -1

                        time.sleep(1)
                        # if pid < 30:
                        if firsttimes == endtimes or firsttimes == 1:
                            plheaders = {"Referer": "" + item['sp_url'] + ""}
                            # canshu1 = "http://club.jd.com/comment/getSkuProductPageComments.action?productId="
                            # canshu1 = "http://club.jd.com/comment/productPageComments.action?productId="
                            # canshu2 = "&score=0&sortType=6&pageSize=10" # &page=0
                            canshu1 = "https://club.jd.com/comment/skuProductPageComments.action?productId="  # wgh 2017-9-6
                            canshu2 = "&score=0&sortType=6&pageSize=10"
                            spplurl = canshu1 + productid + canshu2 + "&page=" + str(pagenum)
                            yield Request(spplurl, callback=self.parseContentJD, headers=plheaders, dont_filter=True,
                                              meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                                    'pagenum': pagenum,'id':{'pid':pid,'uid':uid,'fid':fid},'starturl':starturl,'attr':attr})
                        else:
                            print pid
                            print pagenum
                            print u'此页数据采集完成'
                    else:
                        print u'京东 pljson 错误'
                        attr = response.meta['attr']
                        strtime = str(datetime.datetime.now())
                        attr['url'] = starturl
                        attr['crawltime']= strtime
                        data = attr
                        key = "no_comment"
                        k = mysql_submit(data=data, key=key)
                        print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
                except Exception, ex:
                    error_msg = traceback.format_exc()
                    print error_msg
                    attr = response.meta['attr']
                    strtime = str(datetime.datetime.now())
                    attr['url'] = starturl
                    attr['crawltime']= strtime
                    data = attr
                    key = "no_comment"
                    k = mysql_submit(data=data,key=key)
                    print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url
            self.log(error_msg.decode('gbk'),level=logging.ERROR)
            self.log("Response_url error:" + str(response.url), level=logging.ERROR)

    # 苏宁易购
    def parseSN(self, response):
        try:
            spurl = response.url
            spname = response.xpath('//h1[@id="itemDisplayName"]/text()|//div[@class="proinfo-title"]/h1/text()').extract()
            partNumber = re.search('"partNumber":"(?P<dd>\d+)"', response.body)
            vendorCode = re.search('"vendorCode":"(?P<dd>\d+)"', response.body)
            if partNumber:
                if vendorCode:
                    productid = 'general-' + str(partNumber.group('dd')) + '-' + str(vendorCode.group('dd'))
                else:
                    productid = 'style-' + str(partNumber.group('dd')) + '-'
            else:
                print 'partNumber'
                print response.url
            # spplurltemp = ('http://review.suning.com/ajax/review_lists/_pid_'
            #                '-total-_p_-default-10-----reviewList.htm?callback=reviewList')
            # plheaders = {"Referer":str(spurl),"Host":"review.suning.com","Connection":"keep-alive"}
            spplurltemp = ('http://review.suning.com/ajax/review_lists/_pid_'
                           '-total-_p_-default-10-----reviewList.htm?callback=reviewList')
            plheaders = {"Referer": str(spurl), "Host": "review.suning.com", "Connection": "keep-alive"}
            item = AvccollectionagentItem()
            item['attr'] = response.meta['attr']
            item['sp_url'] = response.meta['sp_url']
            if spname and spname[0] and len(spname)>1:
                spname = spname[1]
            else:
                spname = spname[0]
            item['sp_name'] = spname.strip()
            id = str(spurl).split('/')[-1].strip().split('.')[0]
            s_name = shop_name_suning(id)
            if s_name:
                item['sp_dianp'] = s_name.strip()
            else:
                url_dianp = response.xpath('//strong[@id="curShopName"]/a/text()').extract()
                item['sp_dianp'] = url_dianp[0].strip() if url_dianp else ""
            canshudata = response.xpath('//div[@id="appraise"]/a/@href').extract()
            canshu2 = canshudata[0].strip().split('/')[-1].split('-1-')[0].strip()
            # canshu1 = "http://review.suning.com/ajax/review_lists/"
            # canshu3 = "-total-1-timeSort-10-----reviewList.htm?callback=reviewList"
            canshu1 = "http://review.suning.com/ajax/review_lists/"
            canshu3 = "-total-1-timeSort-10-----reviewList.htm?callback=reviewList"
            spplurl = canshu1 + canshu2.strip() + canshu3
            attr = response.meta['attr']
            starturl = response.meta['sp_url']
            item['cx_info'] = ""
            baseinfo = suning_base_info(spurl)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            yield Request(spplurl, callback=self.parseContentSN, headers=plheaders, dont_filter=True,
                                  meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid, 'pagenum': '1'
                                        ,'id':{"pid":0,"uid":0},'starturl':starturl,'canshu':canshu2,'attr':attr
                                        })
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url
            attr = response.meta['attr']
            strtime = str(datetime.datetime.now())
            attr['url'] = response.meta['sp_url']
            attr['crawltime']= strtime
            data = attr
            key = "bf_url"
            k = mysql_submit(data=data,key=key)
            print u'被封 数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10

    def parseContentSN(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        pid = response.meta['id']['pid']
        starturl = response.meta['starturl']
        canshudata = response.meta['canshu']
        attr = response.meta['attr']
        handle_httpstatus_list = [403]
        plheaders = {"Referer":str(starturl),"Host":"review.suning.com"}
        nocomment = []
        # wgh add 2017-09-11
        firsttimes = 0  # 判断第一次出现的评论的日期范围（7天）
        # endtimes = 0  # 最后一次查询评论的日期范围（7天）

        if response.status == 403:
            spplurl = response.url
            print u'网站被封...休息3秒钟，继续爬'
            strtime = str(datetime.datetime.now())
            attr['url'] = starturl
            attr['crawltime']= strtime
            data = attr
            key = "no_comment"
            k = mysql_submit(data=data,key=key)
            print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
        else:
            try:
                html = str(response.body)
                html = html[html.find('(') + 1:html.rfind(')')]
                pljsons = json.loads(html)
                pljson = pljsons['commodityReviews']
                if len(pljson) > 0:
                    for pljsoninfo in pljson:
                        iteminfo = AvccollectionagentItem()
                        try:
                            iteminfo['sp_url'] = item['sp_url']
                            iteminfo['sp_name'] = item['sp_name']
                            iteminfo['sp_maijia'] = pljsoninfo['userInfo']['nickName']
                            iteminfo['sp_pl'] = pljsoninfo['content']
                            iteminfo['sp_plriqi'] = pljsoninfo['publishTime']
                            iteminfo['attr'] = item['attr']
                            iteminfo['sp_dianp'] = item['sp_dianp'] if item['sp_dianp'] else u'苏宁自营'
                            iteminfo['productColor'] = ""
                            iteminfo['sp_score']  = pljsoninfo['qualityStar']
                            iteminfo['sp_brand'] = item['sp_brand']
                            iteminfo['sp_models'] = item['sp_models']
                            iteminfo['color'] = item['color']
                            iteminfo['sp_web_price'] = item['sp_web_price']
                            iteminfo['cx_info'] = item['cx_info']
                            # 增加回复
                            url_id = pljsoninfo['commodityReviewId']
                            url = "http://review.suning.com/ajax/reply_list/%s--1-replylist.htm"%str(url_id).strip()
                            # 测试 url
                            replieshtml = replies_suning(url)
                            # if u'无回复数据' in requests.get(url).text:
                            if u'无回复数据' in replieshtml:
                                iteminfo['replies'] = ""
                            else:
                                htmltext = replieshtml.strip()
                                time.sleep(0.5)
                                text = re.search('\((?P<connect>.*)\)',htmltext).group('connect')
                                text_dict = json.loads((text))['replyList'][0]['replyList']
                                text_list = list()
                                for text in text_dict:
                                    data_dict = dict()
                                    if u'苏宁' and u'官方' in text['replyUserNickName']:
                                        data_dict['sp_plriqi'] = text['replyTime'] if text else ""
                                        data_dict['sp_name'] = text['replyUserNickName'] if text else ""
                                        data_dict['sp_pl'] = text['replyContent'] if text else ""
                                        data_dict['official_reply'] = 1
                                        text_list.append(data_dict)
                                    else:
                                        data_dict['official_reply'] = 0
                                        text_list.append(data_dict)
                                iteminfo['replies'] = text_list
                        except Exception, ex:
                            error_msg = traceback.format_exc()
                            print error_msg
                            print response.url
                            attr = response.meta['attr']
                            strtime = str(datetime.datetime.now())
                            attr['url'] = starturl
                            attr['crawltime']= strtime
                            data = attr
                            key = "no_comment"
                            k = mysql_submit(data=data,key=key)
                            print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
                        if str(iteminfo['sp_plriqi']) > old_time:
                            pid = pid + 1
                            firsttimes = 1
                            nocomment.append(str(iteminfo['sp_plriqi']))
                            data = dict(iteminfo)
                            print json.dumps(data, indent=1)
                            key = "result_items"
                            strtime = str(datetime.datetime.now())
                            bf_submit(redisname=self.name,data=data,key=key,strtime=strtime)
                            print u'数据已经备份'
                            k = mysql_submit(data=data,key=key)
                            print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'*10
                            yield iteminfo
                        else:
                            pass
                    if not nocomment and int(pid)==0:
                            attr["url"]= starturl
                            data = attr
                            key = "no_comment"
                            strtime = str(datetime.datetime.now())
                            # bf_submit(redisname=self.name,data=data,key=key,strtime=strtime)
                            print u'无评论数据已上传'
                            k = mysql_submit(data=data,key=key)
                            print u'无评论数据已保存到数据库' if k==1 else  u'数据入库出现问题'*10
                    else:
                        pass
                    if str(iteminfo['sp_plriqi']) > old_time:
                        firsttimes = 1
                        canshu1 = "http://review.suning.com/ajax/review_lists/"
                        # canshu3 = "-total-" + str(pagenum) +"-default-10-----reviewList.htm?callback=reviewList"
                        canshu3 = "-total-" + str(pagenum) + "-timeSort-10-----reviewList.htm?callback=reviewList"
                        spplurl = canshu1 + canshudata + canshu3
                        headers=plheaders
                        yield Request(spplurl, callback=self.parseContentSN, dont_filter=True,
                                      meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid,
                                            'pagenum': pagenum ,'id':{"pid":pid,"uid":0},'starturl':starturl,'canshu':canshudata,'attr':attr})
                    elif firsttimes == 0:
                        canshu1 = "http://review.suning.com/ajax/review_lists/"
                        # canshu3 = "-total-" + str(pagenum) +"-default-10-----reviewList.htm?callback=reviewList"
                        canshu3 = "-total-" + str(pagenum) + "-timeSort-10-----reviewList.htm?callback=reviewList"
                        spplurl = canshu1 + canshudata + canshu3
                        headers = plheaders
                        yield Request(spplurl, callback=self.parseContentSN, dont_filter=True,
                                      meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid,
                                            'pagenum': pagenum, 'id': {"pid": pid, "uid": 0}, 'starturl': starturl,
                                            'canshu': canshudata, 'attr': attr})
                    else:
                        print u'此页数据采集完成'
                else:
                    print u"len(pljson)---小于0"
                    print response.url
                    attr = response.meta['attr']
                    strtime = str(datetime.datetime.now())
                    attr['url'] = starturl
                    attr['crawltime']= strtime
                    data = attr
                    key = "no_comment"
                    k = mysql_submit(data=data,key=key)
                    print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
            except Exception, ex:
                error_msg = traceback.format_exc()
                print u"html[html.find('(') + 1:html.rfind(')')]--错误"
                print error_msg
                print response.url
                attr = response.meta['attr']
                strtime = str(datetime.datetime.now())
                attr['url'] = starturl
                attr['crawltime']= strtime
                data = attr
                key = "no_comment"
                k = mysql_submit(data=data,key=key)
                print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10

    # 国美在线
    def parseGM(self, response):
        sxurl = response.meta['sp_url']
        sx_attr=response.meta['attr']
        if 'ep.gome.com' in response.url:shixiaourl(url=sxurl,attr=sx_attr)
        try:
            spurl = response.url
            spname = response.xpath('//*[@id="gm-prd-main"]/li[1]/h1/text()|\
                                    //div[@class="hgroup"]/h1/text()')[0].extract()
            try:
                productid = re.search('prdId:"(?P<dd>\d+)"', response.body).group('dd')
            except:
                productid = (response.url).split('/')[-1].split('-')[0].strip()
            # spplurltemp = ('http://ss.gome.com.cn/item/v1/prdevajsonp/appraiseModuleAjax/'
            #                '_pid_/_p_/all/flag/appraise/all?callback=all')
            spplurltemp = ('http://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/'
                           '_pid_/_p_/all/0/flag/appraise/all?callback=all&_={0}').format(int(time.time()*1000))

            plheaders = {"Referer": "" + spurl + ""}
            # add
            item = AvccollectionagentItem()
            item['attr'] = response.meta['attr']
            item['sp_url'] = spurl
            sp_dianp = response.xpath('//div[@class="bte8"]/a/text()|\
                                      //div[@class="bte8"]/span/text()|\
                                      //div[@class="bte8 clearfix"]/a/text()').extract()
            item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp else ""
            item['sp_name'] = spname
            spplurl = spplurltemp.replace('_pid_', productid).replace('_p_', '1')

            urlcanshu1 = "http://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/"
            urlcanshu2 = str(response.url.split('/')[-1].split('.html')[0].strip().replace('-', '/').strip()).split('/')[0]
            urlcanshu3 = "/all/0/flag/appraise/all?callback=all&_={0}".format(int(time.time()*1000))
            spplurl = urlcanshu1 + urlcanshu2 + "/1" + urlcanshu3
            urlcanshu = {"canshu1":urlcanshu1, "canshu2": urlcanshu2, "canshu3": urlcanshu3}
            attr = response.meta['attr']
            starturl = response.meta['sp_url']
            baseinfo = gome_base_info(spurl)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            item['cx_info'] = baseinfo['cx_info']
            yield Request(spplurl, callback=self.parseContentGM, headers=plheaders, dont_filter=True,
                          meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid, 'pagenum': '1',
                                'canshu':urlcanshu,'starturl':starturl,'id':{"pid":0,"uid":0},'attr':attr,'maijia':'110'
                                })
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url
            attr = response.meta['attr']
            strtime = str(datetime.datetime.now())
            attr['url'] = response.meta['sp_url']
            attr['crawltime']= strtime
            data = attr
            key = "bf_url"
            k = mysql_submit(data=data,key=key)
            print u'被封 数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10

    def parseContentGM(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        canshu = response.meta['canshu']
        starturl = response.meta['starturl']
        pid = response.meta['id']['pid']
        urlcanshu1 = canshu['canshu1']
        urlcanshu2 = canshu['canshu2']
        urlcanshu3 = canshu['canshu3']
        attr = response.meta['attr']
        maijia = response.meta['maijia']
        nocomment=[]
        urlcanshu = {"canshu1": urlcanshu1,"canshu2": urlcanshu2,"canshu3": urlcanshu3}
        try:

            pljsons = json.loads(response.body)
            pljson = pljsons['evaList']['Evalist']
            if len(pljson) > 0:
                for pljsoninfo in pljson:
                    iteminfo = AvccollectionagentItem()
                    try:
                        iteminfo['sp_url'] = item['sp_url']
                        iteminfo['sp_name'] = item['sp_name']
                        iteminfo['sp_maijia'] = pljsoninfo['loginname'] if "loginname" in pljsoninfo.keys() else ""
                        iteminfo['sp_pl'] = pljsoninfo['appraiseElSum']
                        iteminfo['sp_plriqi'] = pljsoninfo['post_time'] if len(pljsoninfo['post_time'].split(':'))>2 else pljsoninfo['post_time'] + ":00"
                        iteminfo['sp_score'] = pljsoninfo['mscore']
                        iteminfo['productColor'] = ""
                        iteminfo['attr'] = item['attr']
                        iteminfo['sp_dianp'] = item['sp_dianp'] if item['sp_dianp'] else u'国美自营'
                        iteminfo['sp_brand'] = item['sp_brand']
                        iteminfo['sp_models'] = item['sp_models']
                        iteminfo['color'] = item['color']
                        iteminfo['sp_web_price'] = item['sp_web_price']
                        iteminfo['cx_info']= item['cx_info']
                        if pljsoninfo['gomereply']:
                            data_dict = dict()
                            data_list = list()
                            if u'国美回复' in pljsoninfo['gomereply']['merchant']:
                                data_dict['sp_name'] = pljsoninfo['gomereply']['merchant'] if pljsoninfo['gomereply'] else ""
                                data_dict['sp_plriqi'] = pljsoninfo['gomereply']['time'] if pljsoninfo['gomereply'] else ""
                                data_dict['sp_pl'] = pljsoninfo['gomereply']['text'] if pljsoninfo['gomereply'] else ""
                                data_dict['official_reply'] = 1
                                data_list.append(data_dict)
                            else:
                                data_dict['official_reply'] = 0
                                data_list.append(data_dict)
                            iteminfo['replies'] = data_list if data_list else ""
                        else:
                            iteminfo['replies'] = ""
                    except Exception, ex:
                        error_msg = traceback.format_exc()
                        print error_msg
                        print response.url
                        attr = response.meta['attr']
                        strtime = str(datetime.datetime.now())
                        attr['url'] = starturl
                        attr['crawltime']= strtime
                        data = attr
                        key = "no_comment"
                        k = mysql_submit(data=data,key=key)
                        print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
                    if str(iteminfo['sp_plriqi']) > old_time:
                    # if 1:
                        pid = 0
                        nocomment.append(str(iteminfo['sp_plriqi']))
                        data = dict(iteminfo)
                        key = "result_items"
                        print json.dumps(dict(iteminfo),indent=1)
                        strtime = str(datetime.datetime.now())
                        bf_submit(redisname=self.name,data=data,key=key,strtime=strtime)
                        print u'数据已经备份'
                        k = mysql_submit(data=data,key=key)
                        print u'结果数据已保存到数据库' if k==1 else  u'数据入库出现问题'*10
                        yield iteminfo
                    else:
                        pid +=1

                if str(iteminfo['sp_plriqi']) > old_time and iteminfo['sp_maijia'] != maijia:
                    plheaders = {"Referer": "" + item['sp_url'] + ""}
                    spplurl = urlcanshu1 + urlcanshu2 + "/" + pagenum + urlcanshu3
                    maijia = iteminfo['sp_maijia'] if iteminfo else ""
                    yield Request(spplurl, callback=self.parseContentGM, headers=plheaders, dont_filter=True,
                                      meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid,'maijia':maijia,
                                            'pagenum': pagenum,'canshu':urlcanshu,'starturl':starturl,'attr':attr,'id':{"pid":pid,"uid":0}})
                else:
                    print u'此页数据采集完成'
            else:
                attr = response.meta['attr']
                strtime = str(datetime.datetime.now())
                attr['url'] = starturl
                attr['crawltime']= strtime
                data = attr
                key = "no_comment"
                k = mysql_submit(data=data,key=key)
                print u'无评论数据 保存到数据库' if k==1 else  u'数据入库出现问题'*10
        except Exception, ex:
            error_msg = traceback.format_exc()
            print u'网站可能被封'
            print u'测试3次失败'
            attr["url"] = starturl
            data = attr
            key = "no_comment"
            strtime = str(datetime.datetime.now())
            # bf_submit(redisname=self.name,data=data,key=key,strtime=strtime)
            print u'被封url 已上传'
            k = mysql_submit(data=data,key=key)
            print u'无评论已保存到数据库' if k==1 else  u'数据入库出现问题'

    # 一号店 # 添加 starturl
    def parseYHD(self, response):
        try:
            # ip = response.meta['proxy']
            spurl = response.url
            spname = response.xpath('//*[@id="productMainName"]/text()')
            if spname:
                spname = spname[0].extract()
            else:
                spname = response.xpath('//h1[@id="productMainName"]/text()').extract()
                spname = spname[0].strip if spname else ""
            productid = re.search('"mainProductId" value="(?P<dd>\d+)">', response.body).group('dd')
            plheaders = {
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Cookie":xconfig.YHD_COOKIE,
                    "Host":"e.yhd.com",
                    "Referer": "http://item.yhd.com/item/60909989",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
                }
            # plheaders = {"Cookie":Cookie}
            item = AvccollectionagentItem()
            sp_dianp = response.xpath('//p[@class="key_shop"]/a/text()').extract()
            item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp else u'一号店自营'
            item['sp_url'] = response.meta['sp_url']
            item['attr'] = response.meta['attr']
            item['sp_name'] = spname

            canshu1 = "http://e.yhd.com/front-pe/productExperience/proExperienceAction!ajaxView_pe.do?product.id="
            canshu2 = "&merchantId=201045&filter.orderType=newest&pagenationVO.rownumperpage=5&currSiteId=1&currSiteType=2&filter.commentFlag=total&filter.sortFlag=order_by_createtime&filter.mainProdId=null&filter.labelId=null&peCode=-1"
            param_1 = "&pagenationVO.preCurrentPage="
            canshu3 = "&pagenationVO.currentPage=1"  # 页码
            cc = str(time.ctime()).split(' ')
            strtime = cc[0] +"%20"+ cc[1] +"%20"+ cc[2] +"%20"+ cc[-1] +"%20"+ cc[-2] +"%20"+"GMT+0800"
            tt = "&tt=" + strtime
            spplurl = canshu1 + str(productid) + canshu2 + param_1+"1" + canshu3 + tt + "&_=1478057497522"
            canshudata = {"canshu1":canshu1,"canshu2":canshu2,"canshu3":canshu3,"tt":tt,"param":param_1}
            spplurltemp = spplurl
            item['cx_info'] = ""
            baseinfo = yhd_base_info(spurl)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            yield Request(spplurl, callback=self.parseContentYHD, headers=plheaders, dont_filter=True,
                          meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid, 'pagenum': '1'
                                ,'id':{"pid":0,"uid":0 },"canshu":canshudata,'starturl':str(response.meta['sp_url'])
                                ,'headers':plheaders})
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url

    def parseContentYHD(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        pid = response.meta['id']['pid']
        uid = response.meta['id']['uid']
        starturl = response.meta['starturl']
        canshu = response.meta['canshu']
        headers = response.meta['headers']
        try:
            htmpage = yhd_page(url=starturl,pid=productid,pagenumber=response.meta['pagenum'])
            htmlsource = json.loads(htmpage)
            plhtml = htmlsource['value'] if htmlsource else ""
            texthtml = plhtml.replace('\\','').strip()
            plhtmls = Selector(text=texthtml).xpath('//div[@class="comment_con"]/div[@id="div_pe_clist"]/div')
            if len(plhtmls) > 0:
                    for plhtml in plhtmls:
                        iteminfo = AvccollectionagentItem()
                        try:
                            iteminfo['sp_url'] = item['sp_url']
                            iteminfo['sp_name'] = item['sp_name']
                            iteminfo['sp_dianp'] = item['sp_dianp']
                            iteminfo['productColor'] = ""
                            sp_maijia = plhtml.xpath('div[@class="nameBox"]/span/@username').extract()
                            iteminfo['sp_maijia'] = sp_maijia[0].strip() if sp_maijia else ""
                            sp_score = plhtml.xpath('dl/dt/span[3]/@class').extract()
                            if sp_score:
                                sp_score_a = plhtml.xpath('dl/dt/span[4]/@class').extract()
                                sp_score = sp_score if 'star' in sp_score[0] else sp_score_a
                            iteminfo['sp_score'] = re.search('\d',sp_score[0].strip()).group() if sp_score else ""
                            sp_pl_test = plhtml.xpath('dl//dd[@class="clearfix"]//span[2]//text()').extract()
                            sp_pl = Selector(text=plhtml.extract()).xpath('//span[@class="text"]/text()').extract()
                            iteminfo['sp_pl'] = sp_pl[-1].strip() if sp_pl else ""
                            sp_plriqi = plhtml.xpath('dl/dd[@class="replyBtn_con clearfix"]/span/text()').extract()
                            sp_plriqi = sp_plriqi[0].split(' ') if sp_plriqi else ""
                            iteminfo['sp_plriqi'] = sp_plriqi[-2].strip()+" " + sp_plriqi[-1] if sp_plriqi else ""
                            iteminfo['attr'] = item['attr']
                            iteminfo['sp_brand'] = item['sp_brand']
                            iteminfo['sp_models'] = item['sp_models']
                            iteminfo['color'] = item['color']
                            iteminfo['sp_web_price'] = item['sp_web_price']
                            iteminfo['cx_info'] = item['cx_info']
                            # 增加回复
                            replies = Selector(text=plhtml.extract()).xpath('//dl/dd[@class="interReply_box"]/ul[@class="reply_list"]/li[@class="businessReply"]')
                            if replies:
                                time_1 = Selector(text=replies[0].extract()).xpath('//p[@class="time"]/text()').extract()
                                name = Selector(text=replies[0].extract()).xpath('//p[@class="user"]/span[1]/text()').extract()
                                con = Selector(text=replies[0].extract()).xpath('//p[@class="user"]/span[3]/text()').extract()
                                data_list = list()
                                data_dict = dict()
                                if u'1号店' and u'官方' and u'1号店官方' in name[0]:
                                    data_dict['sp_plriqi'] = time_1[0].strip() if time_1 else ""
                                    data_dict['sp_name'] = name[0].strip() if name else ""
                                    data_dict['sp_pl'] = con[0].strip() if con else ""
                                    data_dict['official_reply'] = 1
                                    data_list.append(data_dict)
                                    iteminfo['replies'] = data_list
                                else:
                                    iteminfo['replies'] = ""
                            else:
                                iteminfo['replies'] = ""
                            print json.dumps(dict(iteminfo),indent=1)
                        except Exception, ex:
                            error_msg = traceback.format_exc()
                            print error_msg
                            print response.url
                        # if len(iteminfo['sp_plriqi'])>0:
                        if str(iteminfo['sp_plriqi']) > old_time:
                        # if 1:
                                pid = 0
                                uid = int(uid) + 1
                                data = json.dumps(dict(iteminfo),indent=1)
                                print data
                                data = dict(iteminfo)
                                result_data = dict(iteminfo)
                                key = "result_items"
                                bf_submit(redisname=self.name,data=data,key=key,strtime="")
                                mysql_result = mysql_submit(result_data,key)
                                print u'一号店数据已备份到数据库' if mysql_result ==1 else u'一号店备份数据入库出现问题'
                                yield iteminfo
                        else:
                            pass
                    else:
                            pass
                    if int(uid) == 0:
                        key = "no_comment"
                        crawltime = str(datetime.datetime.now())
                        data = item['attr']
                        data['url'] = starturl
                        data['crawltime'] = crawltime
                        mysql_result = mysql_submit(data,key)
                        print u'一号店无评论数据已备份到数据库' if mysql_result ==1 else u'一号店无评论数据入库出现问题'
                    else:
                        pass
                    if str(iteminfo['sp_plriqi']) > old_time:
                    # if 1:
                            pagecanshu = '&pagenationVO.currentPage=' + str(pagenum)
                            cc = str(time.ctime()).split(' ')
                            strtime = cc[0] +"%20"+ cc[1] +"%20"+ cc[2] +"%20"+ cc[-1] +"%20"+ cc[-2] +"%20"+"GMT+0800"
                            tt = "&tt=" + strtime
                            param_1 = canshu['param']
                            canshudata = {"canshu1":canshu['canshu1'],"canshu2":canshu['canshu2'],"canshu3":pagecanshu,"tt":tt,"param":param_1}
                            spplurl = canshu['canshu1'] + str(productid) + canshu['canshu2'] + param_1+ str(int(pagenum)-1)+ pagecanshu + tt +"&_=1478057497522"
                            spplurltemp = spplurl
                            print spplurl
                            yield Request(spplurl, callback=self.parseContentYHD, headers=headers, dont_filter=True,
                                          meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid, 'pagenum':str(pagenum)
                                                ,'id':{"pid":pid,"uid":uid },"canshu":canshudata,'starturl':str(starturl)
                                                ,'headers':headers})
                    else:
                        print u'此页数据采集完成'
            else:
                print u'len(plhtmls) > 0 长度小于 0 '
                key = "bf_url"
                data = item['attr']
                data['url'] = starturl
                mysql_result = mysql_submit(data=data,key=key)
                print u'一号店被封数据已备份到数据库' if mysql_result ==1 else u'一号店被封数据入库出现问题'
        except Exception, ex:
            error_msg = traceback.format_exc()
            print u'网站可能被封'
            print error_msg
            key = "bf_url"
            data = item['attr']
            data['url'] = starturl
            mysql_result = mysql_submit(data=data,key=key)
            print u'一号店被封数据已备份到数据库' if mysql_result ==1 else u'一号店被封数据入库出现问题'

    # 亚马逊
    def parseYMX(self, response):
        try:
            handle_httpstatus_list = [503,404]
            if response.status == 503 or response.status == 404:
                key = "bf_url"
                data = response.meta['attr']
                data['url'] = response.meta['sp_url']
                mysql_result = mysql_submit(data=data,key=key)
                print u'亚马逊被封数据已备份到数据库' if mysql_result ==1 else u'亚马逊被封数据入库出现问题'
                time.sleep(3)
            else:
                spurl = response.url
                spname = response.xpath('//*[@id="productTitle"]/text()|\
                                        //span[@id="ebooksProductTitle"]/text()')[0].extract()
                item = AvccollectionagentItem()
                sp_dianp = response.xpath('//span[@id="ddmMerchantMessage"]/a/text()').extract()
                item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp else u'亚马逊直接销售'
                item['attr'] = response.meta['attr']
                item['sp_url'] = response.meta['sp_url']
                item['sp_name'] = spname.strip()
                url_param = item['sp_url'].split('/')[-1].strip()
                param_1 = "https://www.amazon.cn/product-reviews/"
                param_2 = '/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber=1'
                url = param_1 + url_param.strip() + param_2
                # plheaders = {"Referer": "" + item['sp_url'] + ""}
                # ip = response.meta['proxy']
                # baseinfo = base_info(spurl)
                baseinfo = amazon_base_info(spurl)
                item['sp_brand'] = baseinfo['brand']
                item['sp_models'] = baseinfo['model']
                item['color'] = baseinfo['color']
                item['sp_web_price'] = baseinfo['price']
                item['cx_info'] = ""
                yield Request(url, callback=self.parseContentYMX, dont_filter=True,
                              meta={'item': item, 'spplurltemp': "", 'productid': "", 'pagenum': '1',
                                    'id':{"pid":0,"uid":0 },'spplurltemp':url,'starturl':item['sp_url']
                                    })
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print item['sp_url']

    def parseContentYMX(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-010-02
        pid = response.meta['id']['pid']
        starturl = response.meta['starturl']
        try:
            plhtml = response.xpath('//*[@id="cm_cr-review_list"]')
            if len(plhtml) > 0:
                plhtmls = plhtml[0].xpath('./div/div')
                if len(plhtmls):
                    for plhtml in plhtmls:
                        iteminfo = AvccollectionagentItem()
                        try:
                            iteminfo['sp_url'] = item['sp_url']
                            iteminfo['sp_name'] = item['sp_name']
                            # sp_score = plhtml.xpath('div[@class="a-row"][1]/a/i/@class').extract()
                            sp_score = plhtml.xpath('./div[@class="a-row"][1]/a[1]/i/span/text()').extract()
                            # sp_score = re.search('\d', sp_score[0].strip()).group() if sp_score else ""
                            sp_score = re.search('\d', sp_score[0].strip()).group() if sp_score else ""
                            iteminfo['sp_score'] = sp_score if sp_score else ""
                            # sp_maijia = plhtml.xpath('div[@class="a-row"][2]/span[1]/a/text()').extract()
                            sp_maijia = plhtml.xpath(
                                './div[@class="a-row"][2]/span[@class="a-size-base a-color-secondary review-byline"]/a/text()').extract()
                            iteminfo['sp_maijia'] = sp_maijia[0].strip() if sp_maijia else ""
                            # pl_riqi = plhtml.xpath('div[@class="a-row"][2]/span[4]/text()').extract()
                            pl_riqi = plhtml.xpath(
                                'div[@class="a-row"][2]/span[@class="a-size-base a-color-secondary review-date"]/text()').extract()
                            rq = re.findall('\d+', pl_riqi[0].strip()) if pl_riqi else ""
                            rq = rq[0] + "-" + rq[1] + "-" + rq[2]
                            p3 = time.strftime("%Y-%m-%d", time.strptime(rq.strip(), "%Y-%m-%d"))
                            iteminfo['sp_plriqi'] = p3.strip() + " " + "00:00:00" if len(p3) == 10 else ""
                            # sp_pl = plhtml.xpath('div[@class="a-row review-data"]/span/text()|\
                            #                      div[@class="a-row review-data"]/div/div/span/text()').extract()
                            sp_pl = plhtml.xpath('div[@class="a-row review-data"]/span/text()|\
                                                                             div[@class="a-row review-data"]/div/div/span/text()').extract()
                            iteminfo['sp_pl'] = sp_pl[0].strip() if sp_pl else ""
                            iteminfo['sp_dianp'] = item['sp_dianp']
                            iteminfo['attr'] = item['attr']
                            iteminfo['sp_brand'] = item['sp_brand']
                            iteminfo['sp_models'] = item['sp_models']
                            iteminfo['color'] = item['color']
                            iteminfo['sp_web_price'] = item['sp_web_price']
                            iteminfo['productColor'] = ""
                            iteminfo['cx_info'] = ""
                            rep_name = Selector(text=plhtml.extract()).xpath('//span[1]/text()').extract()
                            if rep_name and u'亚马逊' and u'官方' and u'亚马逊官方' in rep_name[0].strip():
                                replies = Selector(text=plhtml.extract()).xpath(
                                    '//span[@class="review-comment-text"]//text()').extract()
                                data_dict = dict()
                                data_list = list()
                                data_dict['sp_pl'] = replies[0].strip() + replies[1].strip() if replies else ""
                                data_dict['sp_plriqi'] = iteminfo['sp_plriqi'] if iteminfo['sp_plriqi'] else ""
                                data_dict['sp_name'] = rep_name[0].strip() if rep_name else ""
                                data_dict['official_reply'] = 1
                                data_list.append(data_dict)
                                iteminfo['replies'] = data_list
                            else:
                                iteminfo['replies'] = ""
                        except Exception, ex:
                            error_msg = traceback.format_exc()
                            print error_msg
                            print response.url
                        if p3 > str(old_time):
                        # if 1:
                            pid = int(pid) + 1
                            data = json.dumps(dict(iteminfo), indent=1)
                            print data
                            result_data = dict(iteminfo)
                            key = "result_items"
                            bf_submit(redisname=self.name, data=result_data, key=key, strtime="")
                            mysql_result = mysql_submit(result_data, key)
                            print u'亚马逊数据已备份到数据库' if mysql_result ==1 else u'亚马逊备份数据入库出现问题'
                            yield iteminfo
                        else:
                            pass
                    if int(pid)<=0:
                        key = "no_comment"
                        crawltime = str(datetime.datetime.now())
                        data = item['attr']
                        data['url'] = starturl
                        data['crawltime'] = crawltime
                        mysql_result = mysql_submit(data,key)
                        print u'亚马逊无评论数据已备份到数据库' if mysql_result ==1 else u'亚马逊无评论数据入库出现问题'
                    else:
                        pass
                    if p3 > str(old_time) and pid !=0:
                            url_param_1 = spplurltemp.split('pageNumber')[0].strip()
                            url_param_2 = "pageNumber=" + str(pagenum)
                            url = url_param_1 + url_param_2
                            yield Request(url, callback=self.parseContentYMX, dont_filter=True,
                              meta={'item': item, 'spplurltemp': "", 'productid': "", 'pagenum': pagenum,
                                    'id':{"pid":pid,"uid":0 },'spplurltemp':url,'starturl':starturl
                                    })
                    else:
                        print u'此页数据采集完成'
                else:
                    print u'亚马逊len(plhtmls) > 2 长度小于 2'
                    key = "bf_url"
                    data = item['attr']
                    print data
                    data['url'] = starturl
                    mysql_result = mysql_submit(data=data,key=key)
                    print u'亚马逊被封数据已备份到数据库' if mysql_result ==1 else u'亚马逊被封数据入库出现问题'

            else:
                print 'len(plhtml) > 0 长度小于 0 '
                key = "bf_url"
                data = item['attr']
                data['url'] = starturl
                mysql_result = mysql_submit(data=data,key=key)
                print u'亚马逊被封数据已备份到数据库' if mysql_result ==1 else u'亚马逊被封数据入库出现问题'
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg

    # 当当网
    def parseDD(self, response):
        try:
            spurl = response.url
            spname = response.xpath('//*[@id="main_bd"]/div[2]/div[1]/div[2]/div/div[2]/h1/text()')
            if spname:
                spname = spname[0].extract()
            else:
                spname = response.xpath('//div[@class="name_info"]/h1/@title').extract()
                spname = spname[0].strip() if spname else ""
            productid = re.search('\d+', spurl).group()
            spplurltemp = ('http://product.dangdang.com/comment/comment.php?product_id=_pid_'
                           '&datatype=1&page=_p_&filtertype=1&sysfilter=1&sorttype=1')
            item = AvccollectionagentItem()
            item['attr'] = response.meta['attr']
            item['sp_url'] = response.meta['sp_url']
            sp_dianp = response.xpath('//div[@class="show_merchant_inner"]//a[@class="name"]/text()|\
                                      //span[@class="title_name"]/span[@class=""]/a//text()').extract()
            item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp else ""
            item['sp_name'] = spname
            spplurl = spplurltemp.replace('_pid_', productid).replace('_p_', '1')
            plheaders = {
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "X-Requested-With":"XMLHttpRequest",
                "Accept-Encoding":"Accept-Encoding",
                "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection":"keep-alive",
                "Host":"product.dangdang.com",
                "Referer":str(item['sp_url'].strip()),
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
            }
            productid = str(item['sp_url']).split('/')[-1].split('.')[0].strip()
            url_param_1 = "http://product.dangdang.com/?r=callback%2Fcomment-list&productId="
            url_param_2 = "&categoryPath=58.82.19.00.00.00&mainProductId="
            url_param_3 = "&mediumId=12&sortType=2&filterType=1&isSystem=0&tagId=0&pageIndex=1"
            spplurl = url_param_1 + str(productid) + url_param_2 + str(productid) + url_param_3
            # ip = response.meta['proxy']
            # cx_info = response.xpath('//span[@class="head_title_name"]/@title').extract()
            # item['cx_info'] = cx_info[0].strip() if cx_info else ""
            item['cx_info'] = ""
            # baseinfo = base_info(spurl)
            baseinfo = dangdang_base_info(spurl)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            yield Request(spplurl, callback=self.parseContentDD, headers=plheaders, dont_filter=True,
                          meta={'item': item, 'spplurltemp': spplurl, 'productid': productid, 'pagenum': '1',
                          'id':{"pid":0,"uid":0 },'starturl':str(item['sp_url']),'headers':plheaders })
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            key = "bf_url"
            data = item['attr']
            data['url'] = response.meta['sp_url']
            mysql_result = mysql_submit(data=data,key=key)
            print u'当当网被封数据已备份到数据库' if mysql_result ==1 else u'当当网被封数据入库出现问题'

    def parseContentDD(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        pid = response.meta['id']['pid']
        uid = response.meta['id']['uid']
        starturl = response.meta['starturl']
        headers = response.meta['headers']
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-07-07
        time.sleep(1)
        try:
                data = json.loads(response.body)
                pl_regex = data['data']['html']
                htmlsouce = str(pl_regex.strip()).replace('\\', '')
                divs = Selector(text=htmlsouce).xpath('//div[@class="comment_items clearfix"]')
                for div in divs:
                    iteminfo = AvccollectionagentItem()
                    # sp_maijia = div.xpath('./div[@class="items_left"]/p[@class="items_left_name"]/text()').extract()
                    sp_maijia = div.xpath('./div[@class="items_left_pic"]/span[@class="name"]/text()').extract()
                    iteminfo['sp_maijia'] = sp_maijia[0].strip() if sp_maijia else ""
                    # sp_pl = div.xpath('./div[@class="items_right"]/div[@class="items_detail"]/p[@class="describe_detail"]//text()').extract()
                    sp_pl = div.xpath('./div[@class ="items_right"]/div[@ class ="describe_detail"]/span/text()').extract()
                    iteminfo['sp_pl'] = sp_pl[0].strip() if sp_pl else ""
                    # pl_time = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="starline"]/span[1]/text()').extract()
                    pl_time = div.xpath('./div[@class="items_right"]/div[@class="starline clearfix"]/span[1]/text()').extract()
                    # productColor = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="starline"]/span[2]/text()').extract()
                    # productColor = div.xpath('./div[@class="items_right"]/div[@class="starline clearfix"]/span[2]/text()').extract()
                    pl_times = re.search('[\d\s\-\:]+',pl_time[0]).group() if pl_time else ""
                    iteminfo['sp_plriqi'] = pl_times if pl_times else ""
                    # iteminfo['productColor'] = productColor[0].strip() if productColor else ""
                    iteminfo['attr'] = item['attr']
                    iteminfo['sp_score'] = ""
                    iteminfo['sp_url'] = item['sp_url']
                    iteminfo['sp_name'] = item['sp_name']
                    iteminfo['sp_dianp'] = item['sp_dianp'] if item['sp_dianp'] else u'当当自营'
                    iteminfo['sp_brand'] = item['sp_brand']
                    iteminfo['sp_models'] = item['sp_models']
                    iteminfo['color'] = item['color']
                    iteminfo['sp_web_price'] = item['sp_web_price']
                    iteminfo['cx_info'] = item['cx_info']
                    replies_name = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="comment_add comment_seller"]/div[@class="comment_add_line"]/span/text()').extract()
                    replies_content = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="comment_add comment_seller"]/div[@class="comment_add_line"]/text()').extract()
                    if replies_name:
                        data_dict = dict()
                        data_list = list()
                        if u'商家' in str(replies_name[0].strip()):
                            data_dict['sp_pl'] = replies_content[0].strip() if replies_content else ""
                            data_dict['sp_plriqi'] = iteminfo['sp_plriqi'] if iteminfo['sp_plriqi'] else ""
                            data_dict['sp_name'] = replies_name[0].strip() if replies_name else ""
                            data_dict['official_reply'] = 1
                            data_list.append(data_dict)
                            iteminfo['replies'] = data_list
                        else:
                            iteminfo['replies'] = ""
                    else:
                        iteminfo['replies'] = ""
                    if len(iteminfo['sp_plriqi']) > 0 and str(iteminfo['sp_plriqi']) > old_time:
                        uid = int(uid) + 1
                        data = json.dumps(dict(iteminfo),indent=1)
                        print data
                        result_data = dict(iteminfo)
                        key = "result_items"
                        # wgh change 2017-09-05,弃用备份数据
                        bf_submit(redisname=self.name,data=result_data,key=key,strtime="")
                        mysql_result = mysql_submit(result_data, key)
                        print u'当当网数据已备份到数据库' if mysql_result ==1 else u'当当网备份数据入库出现问题'
                        yield iteminfo
                    else:
                       pass
                if int(uid) == 0:
                    key = "no_comment"
                    crawltime = str(datetime.datetime.now())
                    data = item['attr']
                    data['url'] = starturl
                    data['crawltime'] = crawltime
                    mysql_result = mysql_submit(data,key)
                    print u'当当网无评论数据已备份到数据库' if mysql_result ==1 else u'当当网无评论数据入库出现问题'
                else:
                    pass
                if str(iteminfo['sp_plriqi']) > old_time:
                # if 1:
                    plheaders = headers
                    url_param_1 = spplurltemp.split('pageIndex')[0].strip()
                    pageIndex = "pageIndex=" + str(pagenum)
                    spplurl = url_param_1 + pageIndex
                    yield Request(spplurl, callback=self.parseContentDD, headers=plheaders, dont_filter=True,
                                  meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                        'pagenum': pagenum,'id':{"pid":pid,"uid":0 },'starturl':starturl,'headers':plheaders})
                else:
                    print u'此页数据采集完成'
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print u'网站可能被封'
            if pid < 4:
                pid = pid + 1
                plheaders = headers
                url_param_1 = spplurltemp.split('pageIndex')[0].strip()
                pageIndex = "pageIndex=" + str(pagenum)
                spplurl = url_param_1 + pageIndex
                yield Request(spplurl, callback=self.parseContentDD, headers=plheaders, dont_filter=True,
                              meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                    'pagenum': pagenum,'id':{"pid":pid,"uid":str(uid)},'starturl':starturl,'headers':plheaders})
            else:
                key = "bf_url"
                data = item['attr']
                data['url'] = starturl
                mysql_result = mysql_submit(data=data,key=key)
                print u'当当网被封数据已备份到数据库' if mysql_result ==1 else u'当当网被封数据入库出现问题'

    def parseContentDD_old(self, response):
        item = response.meta['item']
        spplurltemp = response.meta['spplurltemp']
        productid = response.meta['productid']
        pagenum = str(int(response.meta['pagenum']) + 1)
        pid = response.meta['id']['pid']
        uid = response.meta['id']['uid']
        starturl = response.meta['starturl']
        headers = response.meta['headers']
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))
        time.sleep(1)
        try:
                data = json.loads(response.body)
                pl_regex = data['data']['html']
                htmlsouce = str(pl_regex.strip()).replace('\\','')
                divs = Selector(text=htmlsouce).xpath('//div[@class="comment_items clearfix"]')
                for div in divs:
                    iteminfo = AvccollectionagentItem()
                    sp_maijia = div.xpath('./div[@class="items_left"]/p[@class="items_left_name"]/text()').extract()
                    iteminfo['sp_maijia'] = sp_maijia[0].strip() if sp_maijia else ""
                    sp_pl = div.xpath('./div[@class="items_right"]/div[@class="items_detail"]/p[@class="describe_detail"]//text()').extract()
                    iteminfo['sp_pl'] = sp_pl[0].strip() if sp_pl else ""
                    pl_time = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="starline"]/span[1]/text()').extract()
                    productColor = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="starline"]/span[2]/text()').extract()
                    pl_times = re.search('[\d\s\-\:]+',pl_time[0]).group() if pl_time else ""
                    iteminfo['sp_plriqi'] = pl_times if pl_times else ""
                    iteminfo['productColor'] = productColor[0].strip() if productColor else ""
                    iteminfo['attr'] = item['attr']
                    iteminfo['sp_score'] = ""
                    iteminfo['sp_url'] = item['sp_url']
                    iteminfo['sp_name'] = item['sp_name']
                    iteminfo['sp_dianp'] = item['sp_dianp'] if item['sp_dianp'] else u'当当自营'
                    iteminfo['sp_brand'] = item['sp_brand']
                    iteminfo['sp_models'] = item['sp_models']
                    iteminfo['color'] = item['color']
                    iteminfo['sp_web_price'] = item['sp_web_price']
                    iteminfo['cx_info'] = item['cx_info']
                    replies_name = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="comment_add comment_seller"]/div[@class="comment_add_line"]/span/text()').extract()
                    replies_content = div.xpath('./div[@class="items_right"]/div[@class="items_user"]/div[@class="comment_add comment_seller"]/div[@class="comment_add_line"]/text()').extract()
                    if replies_name:
                        data_dict = dict()
                        data_list = list()
                        if u'商家' in str(replies_name[0].strip()):
                            data_dict['sp_pl'] = replies_content[0].strip() if replies_content else ""
                            data_dict['sp_plriqi'] = iteminfo['sp_plriqi'] if iteminfo['sp_plriqi'] else ""
                            data_dict['sp_name'] = replies_name[0].strip() if replies_name else ""
                            data_dict['official_reply'] = 1
                            data_list.append(data_dict)
                            iteminfo['replies'] = data_list
                        else:
                            iteminfo['replies'] = ""
                    else:
                        iteminfo['replies'] = ""
                    if len(iteminfo['sp_plriqi'])>0 and str(iteminfo['sp_plriqi']) > old_time :
                    # if 1:
                        uid = int(uid) + 1
                        data = json.dumps(dict(iteminfo),indent=1)
                        print data
                        result_data = dict(iteminfo)
                        key = "result_items"
                        bf_submit(redisname=self.name,data=result_data,key=key,strtime="")
                        mysql_result = mysql_submit(result_data,key)
                        print u'当当网数据已备份到数据库' if mysql_result ==1 else u'当当网备份数据入库出现问题'
                        yield iteminfo
                    else:
                       pass
                if int(uid) == 0:
                    key = "no_comment"
                    crawltime = str(datetime.datetime.now())
                    data = item['attr']
                    data['url'] = starturl
                    data['crawltime'] = crawltime
                    mysql_result = mysql_submit(data,key)
                    print u'当当网无评论数据已备份到数据库' if mysql_result ==1 else u'当当网无评论数据入库出现问题'
                else:
                    pass
                if str(iteminfo['sp_plriqi']) > old_time:
                # if 1:
                    plheaders = headers
                    url_param_1 = spplurltemp.split('pageIndex')[0].strip()
                    pageIndex = "pageIndex=" + str(pagenum)
                    spplurl = url_param_1 + pageIndex
                    yield Request(spplurl, callback=self.parseContentDD, headers=plheaders, dont_filter=True,
                                  meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                        'pagenum': pagenum,'id':{"pid":pid,"uid":0 },'starturl':starturl,'headers':plheaders})
                else:
                    print u'此页数据采集完成'
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print u'网站可能被封'
            if pid < 4:
                pid = pid + 1
                plheaders = headers
                url_param_1 = spplurltemp.split('pageIndex')[0].strip()
                pageIndex = "pageIndex=" + str(pagenum)
                spplurl = url_param_1 + pageIndex
                yield Request(spplurl, callback=self.parseContentDD, headers=plheaders, dont_filter=True,
                              meta={'item': item, 'spplurltemp': spplurl, 'productid': productid,
                                    'pagenum': pagenum,'id':{"pid":pid,"uid":str(uid)},'starturl':starturl,'headers':plheaders})
            else:
                key = "bf_url"
                data = item['attr']
                data['url'] = starturl
                mysql_result = mysql_submit(data=data,key=key)
                print u'当当网被封数据已备份到数据库' if mysql_result ==1 else u'当当网被封数据入库出现问题'

# 一号店 # 添加 starturl

    def parseYHD_new(self, response):
        try:
            spurl = response.url
            spname = response.xpath('//*[@id="productMainName"]/text()')
            if spname:
                spname = spname[0].extract()
            else:
                spname = response.xpath('//h1[@id="productMainName"]/text()').extract()
                spname = spname[0].strip if spname else ""
            productid = re.search('"mainProductId" value="(?P<dd>\d+)">', response.body).group('dd')
            plheaders = {
                    # "Accept": "*/*",
                    # "Connection": "keep-alive",
                    "Cookie": xconfig.YHD_COOKIE,
                    # "Host": "e.yhd.com",
                    "Referer": response.url,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
            }
            # cookie = {"gc": "194895927"}
            cookie = {"guid": "7RY74KW1TG9U326V8SNCBTF4SCB3UNP7F1XF",
                      "msessionid": "BT8JV78CJD3MQ4RE1H7QJQPSNUV5FCN32SAZ", "gc": "194895927"}
            item = AvccollectionagentItem()
            sp_dianp = response.xpath('//p[@class="key_shop"]/a/text()').extract()
            item['sp_dianp'] = sp_dianp[0].strip() if sp_dianp else u'一号店自营'
            item['sp_url'] = response.meta['sp_url']
            item['attr'] = response.meta['attr']
            item['sp_name'] = spname
            canshu1 = "http://e.yhd.com/front-pe/productExperience/proExperienceAction!ajaxView_pe.do?product.id="
            canshu2 = "&merchantId=1&filter.orderType=newest&pagenationVO.currentPage=1"  # 页数:currentPage
            canshu3 = "&pagenationVO.preCurrentPage=0&pagenationVO.rownumperpage=5&currSiteId=1&currSiteType=1&filter.commentFlag=total&filter.sortFlag=order_by_createtime" # preCurrentPage = 页数-1
            cc = str(time.ctime()).split(' ')
            strtime = cc[0] + "%20" + cc[1] + "%20" + cc[2] + "%20" + cc[-1] + "%20" + cc[-2] + "%20" + "GMT+0800"
            canshu4 = "&tt=" + strtime
            canshu5 = "&isBestCity=0&isFresh=0&filter.pesource=0&filter.mainProdId=null&filter.labelId=null&peCode=-1&callback=checkItemDataHandler&_={0}".format(int(time.time() * 1000))
            spplurl = canshu1 + str(productid) + canshu2 + canshu3 +canshu4 + canshu5
            canshudata = {"canshu1": canshu1, "canshu2": canshu2, "canshu3": canshu3, "canshu4": canshu4, "canshu5": canshu5}
            spplurltemp = spplurl
            item['cx_info'] = ""
            baseinfo = yhd_base_info(spurl)
            item['sp_brand'] = baseinfo['brand']
            item['sp_models'] = baseinfo['model']
            item['color'] = baseinfo['color']
            item['sp_web_price'] = baseinfo['price']
            yield Request(spplurl, callback=self.parseContentYHD, dont_filter=True, cookies=cookie, headers=plheaders,
                          meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid, 'pagenum': '1'
                              , 'id': {"pid": 0, "uid": 0}, "canshu": canshudata, 'starturl': str(response.meta['sp_url'])
                              , 'headers': plheaders, 'dont_merge_cookies': True})
        except Exception, ex:
            error_msg = traceback.format_exc()
            print error_msg
            print response.url

    def parseContentYHD_new(self, response):
        item = response.meta['item']
        productid = response.meta['productid']
        pagenum = response.meta['pagenum']
        old_time = str(datetime.datetime.now() + datetime.timedelta(days=-7))[0:10]  # 截取标准日期格式:2017-07-07
        pid = response.meta['id']['pid']
        uid = response.meta['id']['uid']
        starturl = response.meta['starturl']
        # canshu = response.meta['canshu']
        headers = response.meta['headers']
        # cookie = {"gc": "194895927"}
        cookie = {"guid": "7RY74KW1TG9U326V8SNCBTF4SCB3UNP7F1XF",
                      "msessionid": "BT8JV78CJD3MQ4RE1H7QJQPSNUV5FCN32SAZ", "gc": "194895927"}
        include_date = []
        try:
            gethtml = re.search('({")[\s\S]+("})', str(response.body)).group()
            # print gethtml
            gethtml = json.loads(gethtml)
            plhtml = gethtml['value'] if gethtml else ""
            texthtml = plhtml.replace('\\', '').strip()
            plhtmls = Selector(text=texthtml).xpath('//div[@class="comment_con"]/div[@id="div_pe_clist"]/div')
            if len(plhtmls) > 0:
                for plhtml in plhtmls:
                    iteminfo = AvccollectionagentItem()
                    try:
                        iteminfo['sp_url'] = item['sp_url']
                        iteminfo['sp_name'] = item['sp_name']
                        iteminfo['sp_dianp'] = item['sp_dianp']
                        iteminfo['productColor'] = ""
                        sp_maijia = plhtml.xpath('div[@class="nameBox"]/span/@username').extract()
                        iteminfo['sp_maijia'] = sp_maijia[0].strip() if sp_maijia else ""
                        sp_score = plhtml.xpath('dl/dt/span[3]/@class').extract()
                        if sp_score:
                            sp_score_a = plhtml.xpath('dl/dt/span[4]/@class').extract()
                            sp_score = sp_score if 'star' in sp_score[0] else sp_score_a
                        iteminfo['sp_score'] = re.search('\d', sp_score[0].strip()).group() if sp_score else ""
                        sp_pl_test = plhtml.xpath('dl//dd[@class="clearfix"]//span[2]//text()').extract()
                        sp_pl = Selector(text=plhtml.extract()).xpath('//span[@class="text"]/text()').extract()
                        iteminfo['sp_pl'] = sp_pl[-1].strip() if sp_pl else ""
                        sp_plriqi = plhtml.xpath('dl/dd[@class="replyBtn_con clearfix"]/span/text()').extract()
                        sp_plriqi = sp_plriqi[0].split(' ') if sp_plriqi else ""
                        iteminfo['sp_plriqi'] = sp_plriqi[-2].strip() + " " + sp_plriqi[-1] if sp_plriqi else ""
                        iteminfo['attr'] = item['attr']
                        iteminfo['sp_brand'] = item['sp_brand']
                        iteminfo['sp_models'] = item['sp_models']
                        iteminfo['color'] = item['color']
                        iteminfo['sp_web_price'] = item['sp_web_price']
                        iteminfo['cx_info'] = item['cx_info']
                        iteminfo['replies'] = ""
                        print json.dumps(dict(iteminfo), indent=1)
                    except Exception, ex:
                        error_msg = traceback.format_exc()
                        print error_msg
                        print response.url
                    # if len(iteminfo['sp_plriqi'])>0:
                    if str(iteminfo['sp_plriqi']) > old_time:
                        include_date.append(str(iteminfo['sp_plriqi']))
                        pid = 0
                        uid = int(uid) + 1
                        data = json.dumps(dict(iteminfo), indent=1)
                        print data
                        data = dict(iteminfo)
                        result_data = dict(iteminfo)
                        key = "result_items"
                        # wgh change 2017-09-05,弃用备份数据
                        bf_submit(redisname=self.name, data=data, key=key, strtime="")
                        mysql_result = mysql_submit(result_data, key)
                        print u'一号店数据已备份到数据库' if mysql_result == 1 else u'一号店备份数据入库出现问题'
                        yield iteminfo
                    else:
                        pass
                else:
                    pass
                if int(uid) == 0:
                    key = "no_comment"
                    crawltime = str(datetime.datetime.now())
                    data = item['attr']
                    data['url'] = starturl
                    data['crawltime'] = crawltime
                    mysql_result = mysql_submit(data, key)
                    print u'一号店无评论数据已备份到数据库' if mysql_result == 1 else u'一号店无评论数据入库出现问题'
                else:
                    pass
                if len(include_date) > 0 and include_date[len(include_date) - 1] > old_time:
                    pagenum = int(response.meta['pagenum']) + 1
                    canshu1 = "http://e.yhd.com/front-pe/productExperience/proExperienceAction!ajaxView_pe.do?product.id="
                    canshu2 = "&merchantId=1&filter.orderType=newest&pagenationVO.currentPage={0}".format(pagenum)  # 页数
                    canshu3 = "&pagenationVO.preCurrentPage={0}&pagenationVO.rownumperpage=5&currSiteId=1&currSiteType=1&filter.commentFlag=total&filter.sortFlag=order_by_createtime".format(int(pagenum)-1)  # 页数-1
                    cc = str(time.ctime()).split(' ')
                    strtime = cc[0] + "%20" + cc[1] + "%20" + cc[2] + "%20" + cc[-1] + "%20" + cc[
                        -2] + "%20" + "GMT+0800"
                    canshu4 = "&tt=" + strtime
                    canshu5 = "&isBestCity=0&isFresh=0&filter.pesource=0&filter.mainProdId=null&filter.labelId=null&peCode=-1&callback=checkItemDataHandler&_={0}".format(
                        int(time.time() * 1000))
                    spplurl = canshu1 + str(productid) + canshu2 + canshu3 + canshu4 + canshu5
                    canshudata = {"canshu1": canshu1, "canshu2": canshu2, "canshu3": canshu3, "canshu4": canshu4,
                                  "canshu5": canshu5}
                    spplurltemp = spplurl
                    yield Request(spplurl, callback=self.parseContentYHD, dont_filter=True, cookies=cookie, headers=headers,
                                  meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid,
                                        'pagenum': pagenum,
                                        'id': {"pid": pid, "uid": uid}, "canshu": canshudata, 'starturl': str(spplurl),
                                        'headers': headers, 'dont_merge_cookies': True})
                else:
                    print u'此页数据采集完成'
            else:
                print u'len(plhtmls) > 0 长度小于 0 '
                # if int(pagenum) <= 2:
                canshu1 = "http://e.yhd.com/front-pe/productExperience/proExperienceAction!ajaxView_pe.do?product.id="
                canshu2 = "&merchantId=1&filter.orderType=newest&pagenationVO.currentPage={0}".format(pagenum)  # 页数
                canshu3 = "&pagenationVO.preCurrentPage={0}&pagenationVO.rownumperpage=5&currSiteId=1&currSiteType=1&filter.commentFlag=total&filter.sortFlag=order_by_createtime".format(int(pagenum)-1)  # 页数-1
                cc = str(time.ctime()).split(' ')
                strtime = cc[0] + "%20" + cc[1] + "%20" + cc[2] + "%20" + cc[-1] + "%20" + cc[
                    -2] + "%20" + "GMT+0800"
                canshu4 = "&tt=" + strtime
                canshu5 = "&isBestCity=0&isFresh=0&filter.pesource=0&filter.mainProdId=null&filter.labelId=null&peCode=-1&callback=checkItemDataHandler&_={0}".format(
                    int(time.time() * 1000))
                spplurl = canshu1 + str(productid) + canshu2 + canshu3 + canshu4 + canshu5
                canshudata = {"canshu1": canshu1, "canshu2": canshu2, "canshu3": canshu3, "canshu4": canshu4,
                              "canshu5": canshu5}
                spplurltemp = spplurl
                yield Request(spplurl, callback=self.parseContentYHD, dont_filter=True, cookies=cookie, headers=headers,
                              meta={'item': item, 'spplurltemp': spplurltemp, 'productid': productid,
                                    'pagenum': pagenum
                                  , 'id': {"pid": pid, "uid": uid}, "canshu": canshudata, 'starturl': str(spplurl)
                                  , 'headers': headers, 'dont_merge_cookies': True})
        except Exception, ex:
            error_msg = traceback.format_exc()
            print u'网站可能被封'
            print error_msg
            key = "bf_url"
            data = item['attr']
            data['url'] = starturl
            mysql_result = mysql_submit(data=data, key=key)
            print u'一号店被封数据已备份到数据库' if mysql_result == 1 else u'一号店被封数据入库出现问题'
