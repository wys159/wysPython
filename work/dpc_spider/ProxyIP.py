# -*-coding:utf-8-*-
import  json
import requests
import  redis

#代理IP服务器
SERVER= redis.Redis(host='117.122.192.50', port=6479, db=0)
#key
KEY="proxy:iplist4"
#获取代理IP
class ProxyIP:
    def IPP(self):
        proxy1 = SERVER.srandmember(KEY)
        proxyjson = json.loads(proxy1)
        proxiip = proxyjson["ip"]
        ip={'http':proxiip}
        return ip
    def Session(self):
        # 随机取IP
        proxy1 = SERVER.srandmember(KEY)
        proxyjson = json.loads(proxy1)
        proxiip = proxyjson["ip"]
        sesson = requests.session()
        sesson.proxies = {'http': 'http://' + proxiip, 'https': 'https://' + proxiip}
        return sesson
