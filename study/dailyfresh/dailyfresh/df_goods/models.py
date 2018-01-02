#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
#商品分大类
class TypeInfo(models.Model):
	ttitle=models.CharField(max_length=50)
	isDelete=models.BooleanField(default=False)
#商品
class GoodsInfo(models.Model):
	gtitle=models.CharField(max_length=20)
	gpic=models.ImageField(upload_to='df_goods')
	gpric=models.DecimalField(max_digits=5,decimal_places=2)
	isDelete=models.BooleanField(default=False)
	#单位
	gunit=models.CharField(max_length=20,default='500g')
	#点击量
	gclick=models.IntegerField()
	#商品简介
	gjianjie=models.CharField(max_length=200)
	#商品详情
	gcontent=HTMLField()
	gkucun=models.IntegerField()
	#gadv=models.BooleanField(default=False)
	gtype=models.ForeignKey(TypeInfo)

