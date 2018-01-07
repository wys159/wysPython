#_*_coding:utf-8_*_
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.db import transaction
from df_user import user_decorator
from df_user.models import *
from df_cart.models import *
from  models import *
import datetime
@user_decorator.login
def order(request):
	#查询当前用户
	user=UserInfo.objects.get(id=request.session['user_id'])
	#获取所有以get 传递过来的数据
	get=request.GET
	#当多个条件的并关key相同可通知getlist获取成一个list中
	cart_ids=get.getlist('cart_id')
	#获取过来都 是字符型的，转换成数值型的
	cart_ids1=[int(item) for item in cart_ids]
	#在购物车表中查到所有id的商品
	carts=CartInfo.objects.filter(id__in=cart_ids1)
	#把所传递的数据放到字典里
	context={'title':'提交订单','page_name':1,
			 'carts':carts,'user':user,
			 'cart_ids':','.join(cart_ids),
			 }
	return render(request,'df_order/place_order.html',context)
'''
事务：一旦操作失败则全部退回
1、创建订单对像
2、判断商品库存
3、创建详单对像
4、修改商品库存
5、删除购物车
'''
@transaction.atomic
@user_decorator.login
def order_handle(request):
	#事务保存节点，以便失败后回退
	tran_id=transaction.savepoint()
	#获取商品在购物车内编号 形如 字符”4，5“
	cart_ids=request.POST.get('cart_ids')
	#创建订单对像
	try:
		order=OrderInfo()
		now=datetime.datetime.now()
		uid=request.session['user_id']
		nowtime=now.strftime('%Y%m%d%H%M%S')
		order.oid='%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
		#在当前表字段是外健，保存时必须是外分健表的字段
		order.user_id=uid
		print order.oid
		order.odate=now
		# order.ototal=Decimal(request.POST.get('total'))
		order.ototal = request.POST.get('total')
		order.save()
		#创建详单对像
		cart_ids1=[int(item) for item  in cart_ids.split(',')]
		for id1 in cart_ids1:
			detail=OrderDetailInfo()
			detail.order=order
			#查询购物车信息
			cart=CartInfo.objects.get(id=id1)
			#判断商品库存
			goods=cart.goods
			#若库存大于购买的量
			if goods.gkucun>=cart.count:
				#减少库存，并完善详单
				goods.gkucun=cart.goods.gkucun-cart.count
				goods.save()

				detail.goods_id=goods.id
				detail.price=goods.gpric
				detail.count=cart.count
				detail.save()
				cart.delete()
			else:#如果库存小于购买数量，则回退到之前，并返回到购物车页
				transaction.savepoint_rollback(tran_id)
				conctext1 = {'ok': 1}
				return JsonResponse(conctext1)
		transaction.savepoint_commit(tran_id)
		conctext = {'ok': 0}
	except Exception,e:
		print '===================%s'%e
		transaction.savepoint_rollback(tran_id)
		conctext = {'ok': 2}
	#0为下单成功,1为库不够，2为程序出错
	# return redirect('/user/order/')
	return JsonResponse(conctext)

