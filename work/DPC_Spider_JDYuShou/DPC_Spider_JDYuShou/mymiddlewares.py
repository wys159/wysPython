# -*- coding: UTF-8 -*-
# Created by dev on 16-3-23.

import random
import redis, json
import base64
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from twisted.web._newclient import ResponseNeverReceived
from twisted.internet.error import TimeoutError, ConnectionRefusedError, ConnectError
from scrapy.utils.project import get_project_settings


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.13381.207 Safari/537.36"
    ]
    @classmethod
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware(object):
    settings = get_project_settings()
    REDIS_HOST = settings.get('REDIS_HOST')
    REDIS_PORT = settings.get('REDIS_PORT')
    IP_USER = settings.get('IP_USER')
    IP_PWD = settings.get('IP_PWD')
    proxykeys = settings.get("PROXYKEYS")
    # proxykey = settings.get('PROXY_KEY')
    # 代理池  wgh change 2017-9-8 5个代理池 随机选择某一个
    # proxykeys = ["proxy:iplist", "proxy:iplist", "proxy:iplist"]
    redisclient = redis.Redis(REDIS_HOST, REDIS_PORT)
    DONT_RETRY_ERRORS = (TimeoutError, ConnectionRefusedError, ResponseNeverReceived, ConnectError, ValueError)

    def process_request(self, request=None, spider=None):
        """
        将request设置为使用代理
        """
        try:
            self.redisclient = redis.Redis(self.REDIS_HOST, self.REDIS_PORT)
            proxy = self.redisclient.srandmember(random.choice(self.proxykeys))
            proxyjson = json.loads(proxy)
            ip = proxyjson["ip"]
            sship = proxyjson['sship']
            supplier = proxyjson['supplier']
            hostname = proxyjson['hostname']
            password = proxyjson['password']
            message = 'ip:%s,sship:%s,supplier:%s,hostname:%s,pwd:%s' % (ip, sship, supplier, hostname, password)
            # print message
            # ip = "175.155.244.41:44847"
            proxy_user_pass = "%s:%s" % (self.IP_USER, self.IP_PWD)
            encoded_user_pass = base64.b64encode(proxy_user_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print ip
            request.meta['proxy'] = "http://%s" % ip
            request.meta['message'] = message

        except Exception, ee:
            print '------------------------------', ee

    def process_exception(self, request, exception, spider):
        """
        处理由于使用代理导致的连接异常 则重新换个代理继续请求
        """
        # print '错误类型', exception.message
        if isinstance(exception, self.DONT_RETRY_ERRORS):
            fw = open('ipmessage.txt', 'a')
            fw.writelines(request.meta['message']+'\r\n')
            fw.close()
            self.redisclient = redis.Redis(self.REDIS_HOST, self.REDIS_PORT)
            proxy = self.redisclient.srandmember(random.choice(self.proxykeys))
            proxyjson = json.loads(proxy)
            new_request = request.copy()
            ip = proxyjson["ip"]
            sship = proxyjson['sship']
            supplier = proxyjson['supplier']
            hostname = proxyjson['hostname']
            password = proxyjson['password']
            message = 'ip:%s,sship:%s,supplier:%s,hostname:%s,pwd:%s' % (ip, sship, supplier, hostname, password)
            # ip = "175.155.244.41:44847"
            proxy_user_pass = "%s:%s" % (self.IP_USER, self.IP_PWD)
            encoded_user_pass = base64.b64encode(proxy_user_pass)
            new_request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            new_request.meta['proxy'] = "http://%s" % ip
            new_request.meta['message'] = message
            # print "*" * 20
            # print message
            return new_request


def get_ip():
    try:
        pass
    except Exception, e:
        print e
if __name__ == "__main__":
    a = ProxyMiddleware()
    for i in range(1, 2):
        a.process_request()