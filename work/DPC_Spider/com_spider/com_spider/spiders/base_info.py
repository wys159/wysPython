#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import json
import traceback
import redis
import xconfig
import re
import time
import random
from lxml import etree
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

errorCount = 3


def base_info(url):
    try:
        if 'item.jd.com' in str(url):
            submitdata = jd_base_info(url)
            return submitdata
        elif 'suning.com' in str(url):
            submitdata =suning_base_info(url)
            return submitdata
        elif 'gome.com' in str(url):
            submitdata = gome_base_info(url)
            return submitdata
        elif 'tmall.com' in str(url):
            pass
        elif 'amazon.cn' in str(url):
            submitdata = amazon_base_info(url)
            return submitdata
        elif 'dangdang' in str(url):
            submitdata = dangdang_base_info(url)
            return submitdata
        elif 'yhd' in str(url):
            submitdata = yhd_base_info(url)
            return submitdata
        else:
            print u'url 错误'
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
# 京东
def jd_base_info(spurl,spip):
    try:
        ip = spip
        htmlsorce = base_urllib2(spurl, ip)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = {}
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            dts = text.xpath(xconfig.DTS_XPATH)
            dds = text.xpath(xconfig.DDS_XPATH)
            for dt,dd in zip(dts,dds):
                if u'品牌' in dt:
                    baseinfo['brand'] = dd.strip()
                elif u'型号' in dt:
                    baseinfo['model'] = dd.strip()
                elif u'颜色' in dt:
                    baseinfo['color'] = dd.strip()
            for key in keys:
                if key not in baseinfo.keys():baseinfo[key] = ""
            if baseinfo['brand'] == "" or baseinfo['model'] == "":
                if baseinfo['brand'] == "":
                    print u'brand 为 空'
                    brand = text.xpath(xconfig.JD_brand_PARAM_1)
                    baseinfo['brand'] = brand[0].strip() if brand else ""
                elif baseinfo['model'] == "":
                    # print 'model 为 空'
                    htmlsorce = htmlsorce.decode("gbk", "ignore")
                    mk = u"货号："
                    revalue = "(?<=%s)[\s\S]+?(?=</)" % mk
                    model = re.search(revalue, htmlsorce)
                    if model:
                        model = model.group()
                        baseinfo['model'] = model
                    else:
                        baseinfo['model'] = ""
            else:
                pass
        else:
            print u'京东基本信息源码获取失败'
        # 整合
        time.sleep(1)
        price = jd_base_prise(spurl, spip)
        cx_info = jd_base_cx_info(spurl, ip)
        baseinfo['cx_info'] = cx_info['cx_info']
        baseinfo['price'] = price
        baseinfo['url'] = spurl
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg


def jd_base_prise(url, spip):
    try:
        url_canshu3 = url.split('/')[-1].strip().split('.')[0].strip()
        param_list = [
            "http://p.3.cn/prices/get?type=1&",
            'area=1_72_4137&',
            'pdtk=&pduid=856126327',
            '&pdpin=&pdbp=0',
            '&skuid=J_{}'.format(url_canshu3),
            "&callback=cnp"
        ]
        param_1 = ''.join(param_list)
        text_html = base_urllib2(param_1, spip)
        if text_html:
            price = re.search('"p":"(?P<dd>(.*?))"', text_html)
            price = price.group('dd') if price !=None else ""
        else:
            price = ""
        return price

    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
        price = ""
        return price


def jd_base_cx_info(url, ip=None):
    try:
        url_canshu1 = url.split('/')[-1].strip().split('.')[0].strip()
        url_canshu2 = "https://cd.jd.com/promotion/v2?callback=jQuery4470330&skuId="
        url_canshu3 = "&area=1_72_2799_0&shopId=1000002815&venderId=1000002815&cat=737,794,798&_=1480912895625"
        spurl = url_canshu2 + url_canshu1 + url_canshu3
        text = base_urllib2(spurl, ip)
        text = text.strip().decode('gbk').encode('utf-8')
        if text:
            sp_cx_info = re.findall('"ad":"(.*?)"', text)
            if sp_cx_info:
                if '<' in sp_cx_info[0].strip():
                    sp_cx_info = sp_cx_info[0].strip().split('<')[0].strip()
                    return {"cx_info":sp_cx_info}
                else:
                    return {"cx_info":sp_cx_info[0].strip()}
            else:
                return {"cx_info":""}
        else:
            return {"cx_info":""}

    except Exception,e:
        msg = traceback.format_exc()
        print msg
        return {"cx_info":""}


# 苏宁
def suning_base_info(url):
    try:
        # ip_dict = get_ip()
        # ip = str(ip_dict['ip'])
        ip = ""
        htmlsorce = base_urllib2(url, ip)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            dts = text.xpath(xconfig.SPANS_XPATH)
            dds = text.xpath(xconfig.TDS_XPATH)
            for dt,dd in zip(dts,dds):
                if u'品牌' in dt:
                    baseinfo['brand'] = dd.strip()
                elif u'型号' in dt:
                    baseinfo['model'] = dd.strip()
                elif u'颜色' in dt:
                    baseinfo['color'] = dd.strip()
        else:
            print u'苏宁基本信息源码获取失败'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        # 整合
        price = suning_base_price(url, ip)
        baseinfo['price'] = price
        baseinfo['url'] = url
        print json.dumps(dict(baseinfo), indent=1)
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
        return {"brand": "", "model": "", "color": "", "price": ""}


def suning_base_price(url, ip):
    try:
        urlcanshu1 = 'http://icps.suning.com/icps-web/getAllPriceFourPage/000000000'
        urlcanshu2 = str(url).split('/')[-1].split('.')[0].strip()
        urlcanshu3 = '__010_0100101_1_pc_FourPage.getHisPrice.vhtm'
        spurl = urlcanshu1 + urlcanshu2 + urlcanshu3
        htmlpage = base_urllib2(spurl,ip)
        if htmlpage and 'promotionPrice' in str(htmlpage):
            priceg = re.search('"promotionPrice":"(?P<dd>(.*?))"',str(htmlpage))
            if priceg != None:
                price = priceg.group('dd').strip()
                return price
            else:
                print u'苏宁价格页面获取成功，正则不完善'
                return ""
        else:
            print u'苏宁获取价格源码错误'
            return ""
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
# 国美
def gome_base_info(url):
    try:
        ip_dict = get_ip()
        ip = str(ip_dict['ip'])
        htmlsorce = base_urllib2(url,ip)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            dts = text.xpath(xconfig.GOME_SPANS_1_XPATH)
            dds = text.xpath(xconfig.GOMEI_SPANS_2_XPAHT)
            price_param = text.xpath(xconfig.GOMEI_PRICE)
            for dt,dd in zip(dts,dds):
                if u'品牌' in dt and u'品牌型号' not in dt:
                    baseinfo['brand'] = dd.strip()
                elif u'型号' in dt:
                    baseinfo['model'] = dd.strip()
                elif u'颜色' in dt:
                    baseinfo['color'] = dd.strip()
        else:
            print u'国美基本信息源码获取失败'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        # 整合
        price_dict = gome_base_price(url,price_param[0].strip(),ip)
        baseinfo['price'] = price_dict['price']
        baseinfo['cx_info'] = price_dict['cx_info']
        baseinfo['url'] = url
        print json.dumps(dict(baseinfo),indent=1)
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        return {'price':"",'cx_info':"",'url':"",'brand':"",'model':"",'color':''}
        print error_msg

def gome_base_price(url,price_param,ip):
    try:
        urlcanshu1 = "http://ss.gome.com.cn/item/v1/d/m/store/unite/"
        urlcanshu3 = "/N/11010200/110102002/1/null/flag/item/allStore"
        if price_param:
            params = re.search('verify/(.*?)/flag',price_param).group(1)
            urlcanshu2 = params if params else ""
        else:
            print "get price_param_error"
        spurl = urlcanshu1 + urlcanshu2 + urlcanshu3
        htmlpage = base_urllib2(spurl,ip)
        if htmlpage and 'salePrice' in str(htmlpage):
            priceg = re.search('"salePrice":"(?P<dd>(.*?))"',str(htmlpage))
            # cx_info = re.search('"desc":"(?P<dd>(.*?))<',str(htmlpage))
            # cx_info = cx_info.group('dd').strip() if cx_info !=None else ""
            if priceg != None:
                price = priceg.group('dd').strip()
                print price
                return {"price":price,"cx_info":""}
            else:
                print u'国美价格页面获取成功，正则不完善'
                return {"price":"","cx_info":""}
        else:
            print u'国美获取价格源码错误'
            return {"price":"","cx_info":""}
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
        return {"price":"","cx_info":""}

# 天猫
def tmall_base_info(spurl,ip):
    try:
        htmlsorce = base_urllib2(spurl,ip)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            dts = text.xpath(xconfig.TMALL_THS_XPATH)
            dds = text.xpath(xconfig.TMALL_TDS_XPATH)
            for dt,dd in zip(dts,dds):
                if u'品牌' in dt:
                    baseinfo['brand'] = dd.strip()
                elif u'型号' in dt and u'3C'not in dt:
                    baseinfo['model'] = dd.strip()
                elif u'颜色' in dt:
                    baseinfo['color'] = dd.strip()
            skuidg = re.search('"skuId":"(?P<dd>(.*?))"',str(htmlsorce))
            if skuidg !=None:
                skuid = skuidg.group('dd')
            else:
                skuid = ""
        else:
            print u'天猫基本信息源码获取失败'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        brand = text.xpath('//div[@id="J_BrandAttr"]/div/a/text()')
        brand = brand[0].strip() if brand else ""
        baseinfo['brand'] = baseinfo['brand'] if baseinfo['brand'] else brand
        # 整合
        time.sleep(1)
        baseinfo['url'] = spurl
        price = tmall_base_price(spurl,skuid,ip)
        baseinfo['price'] = price
        c  = json.dumps(dict(baseinfo))
        print c
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg


def tmall_base_price(url, skuid, ip):
    try:
        baseurl = xconfig.TMALL_URL
        param_1 = "&itemId=" + str(str(url).split("=")[-1].strip())
        time_param = str(time.time()).replace('.', '0')
        param_2 = "&cachedTimestamp=" + time_param.strip()
        url = baseurl + param_2 + param_1.strip()
        pagehtml = tmaill_urllib2(url)
        if skuid:
            skuid = skuid
        else:
            print u'天猫 skuid 错误'
            return ""
        if 'priceInfo' in pagehtml:
            price_texts = re.search('\((.*?)\)', pagehtml).group(1)
            pp = str(price_texts.strip().decode("gbk").encode("utf8"))
            price_text = json.loads(pp)
            print type(price_text)
            price_list = price_text['defaultModel']['itemPriceResultDO']['priceInfo'][str(skuid)]['promotionList']
            price = price_list[0]['price']
            print price
            return price
        else:
            print u'天猫价格获取源码失败'
            return ""
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg


def tmaill_urllib2(url):
    try:
        headers = xconfig.HEADER
        headers['Referer'] = url.strip()
        req = urllib2.Request(url, headers=headers)
        htmlpagesource = urllib2.urlopen(req, timeout=10)
        htmlpage = htmlpagesource.read()
        if htmlpage:
            return htmlpage
        else:
            return ""
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg


# 亚马逊
def amazon_base_info(url):
    try:
        ip_dict = get_ip()
        ip = str(ip_dict['ip'])
        htmlsorce = amazon_urllib2(url)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            price = text.xpath(xconfig.AMAZON_PRICE_XPATH)
            if price:
                price = re.search('\d.*',str(price[0].strip())).group()
                print price
            else:
                price = ""
                print u'亚马逊价格为空，XPATH 获取可能失败'
            brand = text.xpath(xconfig.AMAZOU_brand_xpath)
            baseinfo['brand'] = brand[0].strip() if brand else ""
            models = text.xpath(xconfig.AMAZOU_models)
            model = text.xpath(xconfig.AMAZOU_model)
            for name,con in zip(models,model):
                if u'型号' in name:
                    baseinfo['model'] = con.strip()
                elif u'颜色' in name:
                    baseinfo['color'] = con.strip()
        else:
            print u'亚马逊获取页面源代码错误'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        # 整合
        time.sleep(1)
        baseinfo['url'] = url
        baseinfo['price'] = price
        c  = json.dumps(dict(baseinfo))
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
def amazon_urllib2(url):
    try:
        headers = xconfig.AMAZOU_HEADER
        req = urllib2.Request(url, headers=headers)
        htmlpagesource = urllib2.urlopen(req, timeout=10)
        htmlpage = htmlpagesource.read()
        if htmlpage:
            return htmlpage
        else:
            return ""
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg
# 当当网
def dangdang_base_info(spurl):
    try:
        ip_dict = get_ip()
        ip = str(ip_dict['ip'])
        htmlsorce = base_urllib2(spurl, ip)
        htmlsorce = str(htmlsorce).decode('gbk').encode('utf8')
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            brand = Selector(text=htmlsorce).xpath(xconfig.DANGDANG_LI_1_XPATH).extract()
            baseinfo['brand'] = brand[0].strip() if brand else ""
            model_pd = Selector(text=htmlsorce).xpath(xconfig.DANGDANG_LI_PD).extract()
            if not brand:
                model = Selector(text=htmlsorce).xpath(xconfig.DANGDANG_LI_3_XPATH).extract()
                baseinfo['model'] = model[0].split(u'\uff1a')[1] if model else ""
            elif model_pd:
                baseinfo['model'] = ""
            else:
               print '1'
               model = Selector(text=htmlsorce).xpath(xconfig.DANGDANG_LI_2_XPATH).extract()
               baseinfo['model'] = model[0].split(u'\uff1a')[1] if model else ""
            price = Selector(text=htmlsorce).xpath(xconfig.DANGDANG_PRICE).extract()
            baseinfo['price'] = price[0].strip() if price else ""
        else:
            print u'当当网基本信息源码获取失败'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        # 整合
        time.sleep(1)
        baseinfo['url'] = spurl
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg

# 一号店
def yhd_base_info(spurl):
    try:
        ip_dict = get_ip()
        ip = str(ip_dict['ip'])
        htmlsorce = base_urllib2(spurl, ip)
        htmlsorce = str(htmlsorce).strip()
        data = baseinfo = dict()
        keys = ['model','brand','color']
        if htmlsorce:
            text = etree.HTML(htmlsorce)
            dds = text.xpath(xconfig.YHD_DDS_XPATH)
            for dd in dds:
                if u'品牌' in dd:
                    dd = dd.split(u'\uff1a')[-1]
                    baseinfo['brand'] = dd.strip()
                elif u'型号' in dd:
                    dd = dd.split(u'\uff1a')[-1] if dd else ""
                    baseinfo['model'] = dd.strip()
                elif u'颜色' in dd:
                    dd = dd.split(u'\uff1a')[-1] if dd else ""
                    baseinfo['color'] = dd.strip()
            price = text.xpath(xconfig.YHD_PRICE_XPATH)
            if price:
                p = re.search('\d+.*',price[0]).group()
                baseinfo['price'] = p.strip()
            else:
                baseinfo['price'] = ""
        else:
            print u'一号店基本信息源码获取失败'
        for key in keys:
            if key not in baseinfo.keys():baseinfo[key] = ""
        # 整合
        time.sleep(1)
        baseinfo['url'] = spurl
        print json.dumps(dict(baseinfo), indent=1)
        return baseinfo
    except Exception,e:
        error_msg = traceback.format_exc()
        print error_msg


# 通用 urllib2
def base_urllib2(url, ip):
    settings = get_project_settings()
    IP_USER = settings.get('IP_USER')
    IP_PWD = settings.get('IP_PWD')
    isTrue = True
    errorcount = 1
    while isTrue:
        ip = get_ip()
        sship = ip['sship']
        supplier = ip['supplier']
        hostname = ip['hostname']
        password = ip['password']
        ip = str(ip['ip'])
        message = 'ip:%s,sship:%s,supplier:%s,hostname:%s,pwd:%s' % (ip, sship, supplier, hostname, password)
        try:
            if ip:
                ip = str(ip).split('/')[-1]
                print ip
                enable_proxy = True
                proxy_handler = urllib2.ProxyHandler({"http": "http://" + IP_USER + ":" + IP_PWD + "@%s" % ip})
                opener = urllib2.build_opener(proxy_handler)
                urllib2.install_opener(opener)
                req = urllib2.Request(url)
                htmlpagesource = urllib2.urlopen(req, timeout=15)
                htmlpage = htmlpagesource.read()
                if htmlpage:
                    isTrue = False
                    return htmlpage
                else:
                    isTrue = False
                    return ""
            else:
                req = urllib2.Request(url)
                htmlpagesource = urllib2.urlopen(req, timeout=20)
                htmlpage = htmlpagesource.read()
                if htmlpage:
                    isTrue = False
                    return htmlpage
                else:
                    isTrue = False
                    return ""
        except Exception,e:
            error_msg = traceback.format_exc()
            if errorcount >= errorCount:
                isTrue = False
            errorcount = errorcount + 1
            print error_msg
            if "timed out" in error_msg or "Errno 10061" in error_msg:
                isTrue = True
            else:
                isTrue = False


def get_ip():
    settings = get_project_settings()
    proxykeys = settings.get("PROXYKEYS")
    redisclient = redis.Redis(host=xconfig.REDIS_HOST, port=xconfig.REDIS_PORT)
    proxy = redisclient.srandmember(random.choice(proxykeys))
    proxyjson = json.loads(proxy)
    ip = proxyjson["ip"]
    sship = proxyjson['sship']
    supplier = proxyjson['supplier']
    hostname = proxyjson['hostname']
    password = proxyjson['password']
    return {"ip": ip, "sship": sship, "supplier": supplier, "hostname": hostname, "password": password}
    # return {"ip": ip}

if __name__=="__main__":
    url = 'http://item.jd.com/2132431.html'
    print jd_base_prise(url, ip="")
