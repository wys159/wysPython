# -*- coding: utf-8 -*-

# Scrapy settings for DPCSellcountSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DPCSellcountSpider'

SPIDER_MODULES = ['DPCSellcountSpider.spiders']
NEWSPIDER_MODULE = 'DPCSellcountSpider.spiders'

#启用Redis调度存储请求队列1
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#不清除Redis队列、这样可以暂停/恢复 爬取2
# SCHEDULER_PERSIST = True

CONCURRENT_REQUESTS = 5

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html  ProxyMiddleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'DPCSellcountSpider.mymiddlewares.RotateUserAgentMiddleware': 401,
    'DPCSellcountSpider.mymiddlewares.ProxyMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
}

# 禁用cookie
COOKIES_ENABLED = False
# 设置下载延迟
# DOWNLOAD_DELAY = 3

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#将清除的项目在redis进行处理
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 400
}

# REDIS_HOST = '192.168.1.17'
# REDIS_PORT = 6379

REDIS_HOST = '117.23.4.139'
REDIS_PORT = 15480
#
# REDIS_HOST = '192.168.100.200'
# REDIS_PORT = 6379

# PROXY_KEY = 'proxy:iplist3'
PROXY_KEY ="avcip:list"

LOG_LEVEL = 'ERROR'
LOG_FILE = 'spider.log'

# 超时时间
DOWNLOAD_TIMEOUT = 15

# 设置延时
# DOWNLOAD_DELAY = 2

