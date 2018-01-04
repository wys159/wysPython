#_*_coding:utf-8_*_
from django.shortcuts import render
from df_user import user_decorator
@user_decorator.login
def cart(request):
	context={'title':'购物车','page_name':1}
	return render(request,'df_cart/cart.html',context)

@user_decorator.login
def add(request,gid,gcount):


	return