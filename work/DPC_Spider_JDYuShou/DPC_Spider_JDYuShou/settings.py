# -*- coding: utf-8 -*-

# Scrapy settings for com_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DPC_Spider_JDYuShou'
SPIDER_MODULES = ['DPC_Spider_JDYuShou.spiders']
NEWSPIDER_MODULE = 'DPC_Spider_JDYuShou.spiders'
#
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'com_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
HTTPERROR_ALLOWED_CODES=[403,503]
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    # 'com_spider.middlewares.MyCustomSpiderMiddleware': 543,
#
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'com_spider.middlewares.MyCustomDownloaderMiddleware': 544,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    'DPC_Spider_JDYuShou.mymiddlewares.RotateUserAgentMiddleware':401,
    'DPC_Spider_JDYuShou.mymiddlewares.ProxyMiddleware':700,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
}
# DOWNLOADER_MIDDLEWARES = {
#     'XQWJ.mymiddlewares.ProxyMiddleware': 100,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 100,
#     'XQWJ.mymiddlewares.RotateUserAgentMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 500
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
DOWNLOAD_TIMEOUT = 10
# VPSNAME = "test_001"
# LOG_LEVEL = "WARNING"
# LOG_FILE = "scrapy.log"
# 亦庄：ss
# REDIS_HOST = '117.122.192.50'
# REDIS_PORT = '6479'
# 西安
REDIS_HOST = '117.23.4.139'
REDIS_PORT = '15480'
IP_USER = 'avcspider'
IP_PWD = 'aowei123'
# 代理ip key
PROXYKEYS = ["proxy:iplist1", "proxy:iplist", "proxy:iplist"]
# REDIS_HOST = '192.168.100.200'
# REDIS_PORT = 6379
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
