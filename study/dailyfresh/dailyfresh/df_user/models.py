# _*_coding:utf-8_*_
from django.db import models

class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.CharField(max_length=30)
    #收货人的名字
    ushou=models.CharField(max_length=20,default='')
    #收货地址
    uaddress=models.CharField(max_length=100,default='')
    #邮编
    uyoubian=models.CharField(max_length=6,default='')
    #手机号
    uphone=models.CharField(max_length=11,default='')
    #default,blank 是python 层面的约束，不影响表结构，不需要重新迁移
