#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.utils.project import get_project_settings
HEADER = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
        }
# JD
DTS_XPATH='//div[@class="Ptable"]/div[1]/dl//dt/text()|\
          //table[@class="Ptable"]/tr/td[1]/text()'

DDS_XPATH='//div[@class="Ptable"]/div[1]/dl//dd/text()|\
          //table[@class="Ptable"]/tr/td[2]/text()'
JD_brand_PARAM_1='//ul[@id="parameter-brand"]/li/@title'
JD_MODEL_PARAM_1='//ul[@id="parameter2"]/li[5]/@title'
JD_MODEL_PARAM_PD='//ul[@id="parameter2"]/li[5]/text()'


# SUNING
SPANS_XPATH ='//table[@id="itemParameter"]//div[@class="name-inner"]/span/text()'
TDS_XPATH = '//table[@id="itemParameter"]//td[@class="val"]//text()'


# GUOMEI
GOME_SPANS_1_XPATH = '//ul[@class="specbox"]/li/span[@class="specinfo"]//text()'
GOMEI_SPANS_2_XPAHT = '//ul[@class="specbox"]/li/span[2]//text()'
GOMEI_PRICE = '//div[@class="pop-inner"]/img/@_src'

#TMALL

# TMALL_THS_XPATH = '//table[@class="tm-tableAttr"]//th[not(@colspan="2")]//text()'
TMALL_THS_XPATH = '//ul[@id="J_AttrUL"]//li/text()'
TMALL_TDS_XPATH = '//ul[@id="J_AttrUL"]//li/@title'
# TMALL_TDS_XPATH = '//table[@class="tm-tableAttr"]//td[not(@colspan="2")]//text()'

TMALL_URL = "https://mdskip.taobao.com/core/initItemDetail.htm?tryBeforeBuy=false&isRegionLevel=false&sellerPreview=false&isUseInventoryCenter=false&queryMemberRight=true&showShopProm=false&addressLevel=2&tmallBuySupport=true&isForbidBuyItem=false&cartEnable=true&household=false&service3C=true&isSecKill=false&offlineShop=false&isApparel=false&cachedTimestamp=1477549507049&isPurchaseMallPage=false&isAreaSell=false&callback=setMdskip&isg=AkdHo0yssR2vc0OubSeLF0YM1/EQ1Bso&isg2=AqOjllxK_5vK6LOvSOP73nMMM-cqNTfaPdAfTdUBZ4J_FME2XmueKjcMeF_0"

HEADER = {
    "Accept":"*/*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":"mdskip.taobao.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
}
JD_HEADER = {
     "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":"cart.jd.com",
    'X-Requested-With':"XMLHttpRequest",
    'Content-Length':0,
    'Cookie':"""__jdu=720839210; __jda=122270672.720839210.1480928151.1480928151.1480928151.1; __jdb=122270672.1.720839210
                |1.1480928151; __jdc=122270672; __jdv=122270672|direct|-|none|-|1480928151004; ipLocation=%u5317%u4EAC
                ; areaId=1; ipLoc-djd=1-72-2799-0; user-key=fcf7eef5-02dc-46b3-b629-f3ed9b4b2fb3; cd=1""",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
}

# AMAZON

AMAZON_PRICE_XPATH = '//span[@id="priceblock_ourprice"]/text()'
AMAZOU_models = '//div[@class="content"][1]//li/b/text()'
AMAZOU_model = '//div[@class="content"][1]//li/text()'
AMAZOU_brand_xpath = '//a[@id="brand"]/text()'

AMAZOU_HEADER = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection":"keep-alive",
    "Host":"www.amazon.cn",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
}

# DANGDANG
DANGDANG_LI_1_XPATH = '//ul[@class="key clearfix"]/li[1]/a//text()'
DANGDANG_LI_2_XPATH = '//ul[@class="key clearfix"]/li[2]//text()'
DANGDANG_LI_3_XPATH = '//ul[@class="key clearfix"]/li[1]/text()'
DANGDANG_LI_PD = '//ul[@class="key clearfix"]/li[2]/a//text()'
DANGDANG_PRICE = '//p[@id="dd-price"]/text()'

# YHD
YHD_DDS_XPATH = '//dl[@class="des_info clearfix"]//dd/@title'
YHD_PRICE_XPATH = '//del[@id="current_price_del"]/text()'
# YHD_COOKIE = "guid=P1S33TMJ9MZ8Q35AZNT2ZQVM2425QX838XZT; msessionid=19GWTFKY4XVXW6GYD3KK98QR2XNEEUPEFE81; abtest=33; globalServerCookieKey=detail_yhdareas||-1|yihaodian.com.hk; search_browse_history=52372522; provinceId=2; detail_yhdareas=2_1000_32017_%E5%8C%97%E4%BA%AC%3Ci%3E%3C%2Fi%3E_%E5%8C%97%E4%BA%AC%E5%B8%82%3Ci%3E%3C%2Fi%3E_%E6%9C%9D%E9%98%B3%E5%8C%BA%3Ci%3E%3C%2Fi%3E; gc=157660776"
YHD_COOKIE = "guid=7RY74KW1TG9U326V8SNCBTF4SCB3UNP7F1XF;msessionid=BT8JV78CJD3MQ4RE1H7QJQPSNUV5FCN32SAZ;gc=194895927"
yhd_cookie = {"guid": "7RY74KW1TG9U326V8SNCBTF4SCB3UNP7F1XF","msessionid":"BT8JV78CJD3MQ4RE1H7QJQPSNUV5FCN32SAZ", "gc":"194895927"}
settings = get_project_settings()
REDIS_HOST = settings.get('REDIS_HOST')
REDIS_PORT = settings.get('REDIS_PORT')
IP_USER = settings.get('IP_USER')
IP_PWD = settings.get('IP_PWD')
PROXYKEYS = settings.get("PROXYKEYS")
