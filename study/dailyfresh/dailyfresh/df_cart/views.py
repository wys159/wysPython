#_*_coding:utf-8_*_
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from df_user import user_decorator
from df_goods.models import *
from df_user.models import *
from models import *
@user_decorator.login
def cart(request):
	uid = request.session['user_id']
	carts=CartInfo.objects.filter(user_id=int(uid))
	print carts.count()
	context={'title':'购物车','page_name':1,'carts':carts,}
	return render(request,'df_cart/cart.html',context)

@user_decorator.login
def add(request,gid,gcount):# gid 为商品的ID gcount 为购买商品的数量
	#获取当前用户id
	uid=request.session['user_id']
	gid=int(gid)
	gcount=int(gcount)
	#判断购物车表是否存在商品，若存在则数量加一，否则要购买的商品保存到购物车当中
	carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
	if len(carts)>=1:
		cart=carts[0]
		cart.count=cart.count+gcount
	else:
		cart=CartInfo()
		cart.user_id=uid
		cart.goods_id=gid
		cart.count=gcount
	cart.save()
	#如果是ajax请求时返回json ，否则返回到购物车
	if request.is_ajax():
		count=CartInfo.objects.filter(user_id=uid).count()
		return  JsonResponse({'count':count})
	return  redirect('/cart/')

#在购物车页面内编辑数量
@user_decorator.login
def edit(request,gid,gcount):
	gid = int(gid)
	gcount = int(gcount)
	#查到用户在表中的记录并修改
	try:
		carts = CartInfo.objects.get(id=gid)
		carts.count=gcount
		carts.save()
		data={'ok':0}
		print carts.count
	except Exception,e:
		data={'ok':int(carts.count)}
	return JsonResponse(data)
#删除购物车内的商品
@user_decorator.login
def cdel(request,gid):
	uid = request.session['user_id']
	gid = int(gid)
	# 查到用户在表中的记录并修改
	try:
		carts = CartInfo.objects.filter(pk=gid)
		carts.delete()
		data={'ok':0}
	except Exception,e:
		data={'ok':int(carts.count)}
	return JsonResponse(data)
