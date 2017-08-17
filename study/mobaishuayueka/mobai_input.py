# _*_ coding:utf-8 _*_
#==========================
#版本：0.1
#声明:本程序只用于学习交流，其他用途盖不负责
#time:2017-08-16
#author:笑看红尘

#==========================

import sys
import time
from selenium import webdriver

def monthka_ling():
    try:
        print u'开始执行' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        telNumlist =open_file()
        driver = webdriver.PhantomJS(executable_path=r'./phantomjs.exe')

        if len(telNumlist)>0 and len(telNumlist[0])==11:
            for i in telNumlist:
                htmltext = ''
                driver.get('https://event.mobike.com/mc/?src=wph')
                time.sleep(1)
                tel = driver.find_element_by_xpath("id('form')/div/div/input")
                tel.send_keys(i)
                submit = driver.find_element_by_id(u'getCoupon')
                submit.click()
                time.sleep(1)
                htmltext=driver.page_source
                if str(i) in htmltext and len(i)==11:
                    massage=str(i)+u'   领取成功'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
                    print massage
                    saveerrorlog('aftertelnum.txt',massage)
                else:

                    massage = str(i) + u'   失败'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '\n'
                    print massage
                    saveerrorlog('aftertelnum.txt', massage)


        else:
            print u'文件为空'
        print u'结束' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    except Exception,e:
        print u"错误信息是：%s"%e
        saveerrorlog('',e)

def open_file():
    try :
        rfile=open('telnum.txt','r')
        buf = rfile.read().split('\n')
        rfile.close()
        return buf
    except Exception,e:
        print u"错误信息是：%s"%e
        saveerrorlog('',e)


def saveerrorlog(filename,massage):
    # "."表示当前路径 ".." 表示当前路径的上一级
    # path = os.path.abspath("..") + "\\errrorlog\\"
    #path = os.path.abspath(".") +"\\"
    if filename!='aftertelnum.txt':
        filename ="errorlog%s.txt" % time.strftime("%Y-%m-%d", time.localtime())
    try:
        #     # r只读，w可写，a追加
        filetext = open(filename, "a")
        if filename != 'aftertelnum.txt':
            filetext.writelines(
                "%s : " % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "%s \r\n" %massage)
            filetext.close()
        else:
            filetext.writelines(massage.encode('utf-8'))
            filetext.close()
    except Exception, e:
        print u"写入日志也错：%s" % e.message

if __name__=='__main__':
    monthka_ling()
    raw_input('press enter key to exit')
