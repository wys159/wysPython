# -*-coding:utf-8-*-
#======================
# 2017年8月9日 15:55:19
#author: wys
#人生苦短，你要偷懒
#======================
import requests
import re
import  urllib
import  redis
import  json
import time
import threadpool
import urllib3
import _mssql
import decimal
import threading
from multiprocessing import Pool
from connectionsqlserver import *

user_agent='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
headers={'User-Agent':user_agent,
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
         }
#左侧树
menu=["指标"]
#地区
urlArea="http://data.stats.gov.cn/easyquery.htm?m=getOtherWds&dbcode=fsyd&rowcode=zb&colcode=sj&wds=%5B%5D&k1=1502334032226"
urlpost='http://data.stats.gov.cn/easyquery.htm'
payload = {'dbcode': 'fsyd', 'id': 'zb','m':'getTree','wdcode':'zb'}
url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"110000"}]&dfwds=[]'
#这是通过地区url
urlget='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=reg&colcode=sj&wds=[{"wdcode":"reg","valuecode":"%s"}]&dfwds=[{"wdcode":"zb","valuecode":"%s"}]'
#通过指标的url
urlget='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"%s"}]&dfwds=[{"wdcode":"zb","valuecode":"%s"}]'
def spider():
    aredic = spiderArea()
    print aredic
    try:
        post_secondtree=post_list(urlpost,payload)
        #第二层
        for key in  post_secondtree:
            print key
            #二级分类
            secondclassify=key["name"]
            print secondclassify
            payload["id"] = key["id"]
            post_thirdtree = post_list(urlpost, payload)
            #第三层
            for postdict in post_thirdtree:
                threezb=postdict["id"]
                # threezb = "A0102"
                payload["id"] = postdict["id"]
                # 三级分类名
                thirdclassify = postdict["name"]
                if postdict['isParent']:
                # if False:
                    post_thirdtree = post_list(urlpost, payload)
                    for postfourth in post_thirdtree:
                        fourthzb=postfourth["id"]
                        #四级分类名
                        fourthclassify=postfourth["name"]
                        #处理存储
                        # spider_cleanout(fourthzb,secondclassify,thirdclassify,fourthclassify)
                        process_spider(fourthzb,secondclassify,thirdclassify,fourthclassify,aredic)
                else:
                    # 在没有第四层情况下
                    process_spider(threezb, secondclassify, thirdclassify, '',aredic)
    except Exception,e:
        strdub = u"错误信息：%s".encode('utf-8') % e
        print strdub
        wr = SaveErrorLogsFile(strdub)
        wr.saveerrorlogs()


    # req=session.get(url,headers=headers,timeout=10)
    # print url
    # html = req.text
    # req.close()
    # print html


def spiderArea():
    '''取地区放入字典中'''
    while True:
        areadict = {}
        # # 代理
        # session = ProxyIP().Session()
        try:
            req = requests.get(urlArea, headers=headers, timeout=10)
            html = req.text
            req.close()
            # 序列化json
            jsonArea = json.loads(html)
            # 取出地区放进列表
            jsonlist = jsonArea["returndata"][0]["nodes"]
            print jsonlist
            for listkey in jsonlist:
                areadict[listkey['code']] = listkey['name']
            #areadict1={'120000':'天津市'}
            return areadict
        except Exception,e:
            print "地区详细错误信息：%s" % e
#反回抓包列表
def spiderlist(url):
    while True:
        # 代理
        # session = ProxyIP().Session()
        try:
            req = requests.get(url, headers=headers, timeout=10)
            Adata = req.text
            req.close()
            jsonAdata = json.loads(Adata)
            return jsonAdata
        except Exception,e:
            strdub = u"抓包列表错误：%s".encode('utf-8') % e
            print strdub
            wr = SaveErrorLogsFile(strdub)
            wr.saveerrorlogs()
#post 的请求，反回树
def post_list(url,payload):
    r = requests.post(url, data=payload, headers=headers)
    postdata=r.text
    r.close()
    jsonpost= json.loads(postdata)
    return jsonpost


#取数
def spiderData(datalist):
    listcode=[]
    wdnodes =[]

    listdatanodes=datalist["returndata"]["datanodes"]
    listname=datalist["returndata"]["wdnodes"][0]["nodes"]
    for key in listdatanodes:
        code=key["code"].replace("zb.","").replace("reg.","").replace("sj.","")
        # data=key["data"]["data"]
        data=key["data"]["strdata"]
        listdata=[code,data]
        listcode.append(listdata)
        #获取最后一级的分类名，code和单位，
    for key in listname:
        cname=key["cname"]
        zbcode=key["code"]
        unit=key["unit"]
        listcname=[cname,zbcode,unit]
        wdnodes.append(listcname)
    listalldata=[listcode,wdnodes]

    return  listalldata

#整理，并存数
def spider_cleanout(are,zbh,secondclassify,thirdclassify,fourthclassify,aredic):
    print aredic[are]+u"开始"
    listax=[]
    try :
        lasturl=urlget %(are,zbh)
        print lasturl
        # 最后获取的json列表数据
        lastdata = spiderlist(lasturl)
        #洗清后的数据
        listcleanout=spiderData(lastdata)

        for listkey1 in listcleanout[0]:
            codekey = listkey1[0].split("_")
            for listkey in listcleanout[1]:
                if codekey[0]==listkey[1]:
                    lastclassify=listkey[0]
                    unity=listkey[2]
                    if unity=='':
                        unity="%"
                    break
            # 地区
            lastarea = aredic[codekey[1]]
            # 时间
            months = codekey[2][2:4]+'.'+codekey[2][4:6]
            # 数值
            data = listkey1[1]
            if data=='':
                data=0
            listax.append((menu[0].decode('utf-8'), secondclassify, thirdclassify, fourthclassify, lastclassify, lastarea,
                           months, data, unity,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),codekey[1]))
        #写入数据库
        wx = ConnectionSqlServer("insert into {0}("
                                 "indicator,secondclassify,thirdclassify,fourthclassify,"
                                 "Detailedindex,area,months,statistic,unit,writetime,areaid"
                                 ") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(
                                 "datastatisticsproess"))
        wx.inserintosqlserver(listax)
        print aredic[are]+u"结束"
        # print fourthclassify+u"完成"
    except Exception,e:

        strdub = u"存储数据时错误信息：%s".encode('utf-8') % e
        print strdub
        wr = SaveErrorLogsFile(strdub)
        wr.saveerrorlogs()

#使用线程处理
def thread_spider(fourthzb,secondclassify,thirdclassify,fourthclassify,aredic):

    threads = []#存放任务对列
    listc=[]
    threadNum=15#创建的线程数
    #创建线程池
    try :
        '''线程池没整明白函数传数的传递
        pool=threadpool.ThreadPool(1)
        #
        for are in aredic:

            # listc=[((are, ), {}),((fourthzb,),{}),(secondclassify,{}),(thirdclassify,{}),(fourthclassify,{})]
            # threads.append(threading.Thread(target=spider_cleanout, args=(are,fourthzb,secondclassify,thirdclassify,fourthclassify,)))
            threads.append(threadpool.makeRequests(spider_cleanout,[((are,fourthzb,secondclassify,thirdclassify,fourthclassify, ), {})]))
            # threads.append(threadpool.makeRequests(spider_cleanout,
            #                                        [((are,), {})]))

        map(pool.putRequest, threads)
        # for are in aredic:
        #
        #     listc.append(([],None))
        # threads=threadpool.makeRequests(spider_cleanout,listc)
        # [pool.putRequest(req) for req in threads]
        pool.poll()
        # pool.wait()
        '''
        for are  in aredic:
            listc.append(are)

        for j in range(0,len(listc),threadNum):
            startthread=j
            endthread=j+threadNum
            for i in listc[startthread:endthread]:
                threads.append(threading.Thread(target=spider_cleanout,
                                                args=(i, fourthzb, secondclassify, thirdclassify, fourthclassify,)))
            for tx in threads:
                tx.start()
            for tx in threads:
                tx.join()
            #清空任务列表
            threads=[]

    except Exception,e:
        print u"线程错误：%s"%e
#使用进程池处理
def process_spider(fourthzb,secondclassify,thirdclassify,fourthclassify,aredic):
    try:
        process_num = 10  # 创建的进程数
        po=Pool(process_num)
        for are in aredic:
            po.apply_async(spider_cleanout,(are, fourthzb, secondclassify, thirdclassify, fourthclassify,aredic,))

        po.close()
        po.join()

    except Exception,e:
        strdub = u"进程错误信息：%s".encode('utf-8') % e
        print strdub
        wr = SaveErrorLogsFile(strdub)
        wr.saveerrorlogs()
if  __name__=='__main__':
    spider()
    raw_input('press enter key to exit')