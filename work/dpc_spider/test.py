# -*-coding:utf-8-*-
from ProxyIP import *
user_agent='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
headers={'User-Agent':user_agent,
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
         }


def test():
    # session = ProxyIP().Session()
    # url='http://data.stats.gov.cn/easyquery.htm'
    # url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"150000"}]&dfwds=[{"wdcode":"zb","valuecode":"A010101"}]'
    # url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=reg&colcode=sj&wds=[{"wdcode":"reg","valuecode":"150000"}]&dfwds=[{"wdcode":"zb","valuecode":"A010101"}]'
    # {"wdcode": "zb", "valuecode": "A010101"}
    # payload = {'dbcode': 'fsyd', 'id': 'A0101','m':'getTree','wdcode':'zb'}
    # # r = requests.post(url, data=payload,headers=headers)
    # r=session.get(url,headers=headers)
    # print r.text
    list1=[11,22,3,44,55,66,77,88,99,223,45]
    for s in range(0,len(list1),16):
        star=s
        end=s+16
        for i in list1[star:end]:
            print i

if  __name__=='__main__':
    test()
