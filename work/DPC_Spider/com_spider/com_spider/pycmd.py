#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import threading


def cmd():
    os.system("scrapy crawl comment_spider")

if __name__ == '__main__':
    threads = []
    threadcount = 10
    for ai in range(threadcount):
        threads.append(threading.Thread(target=cmd, args=()))
    for tx in threads:
        tx.start()
