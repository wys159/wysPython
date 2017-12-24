# _*_coding:utf-8_*_
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import  *
from hashlib import sha1
def register(request):
    return render(request,'df_user/register.html')
def register_handle(request):
    #接收数据
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')
    #判断两次密码
    if upwd!=upwd2:
        return  redirect('/user/register')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()

    #创建对像并存储注册的记录
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    #注册成功转到登录页
    return redirect('/user/login/')

def register_exsit(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    print count
    print uname
    return JsonResponse({'count':count})

#登录页面
def login(request):
	#读cookies,若无则为空
	uname=request.COOKIES.get('uname','')
	context = {'title': '登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
	return render(request,'df_user/login.html',context)
#处理登录错误时用的是整页刷新，还可以用ajax，用待尝试
def login_handle(request):
	#接收数据
	post=request.POST
	uname=post.get('username')
	upwd=post.get('pwd')
	jizhu=post.get('jizhu','0')#记住用户名，若勾选则为其值，否则默认为0
	print uname+" "+upwd
	#查询库中是否存在用户名，反回一个list 形如['用户名']
	users = UserInfo.objects.filter(uname=uname)
	#判断：若用户名存在，则判断加密后的密码正确否，若正确则转到用户中心
	if len(users)==1:
		s1 = sha1()
		s1.update(upwd)
		upwd3 = s1.hexdigest()
		if upwd3==users[0].upwd:
			red=HttpResponseRedirect('/user/info/')
			#处理记住用户名:若记住则写到cookie中，否则删除
			if jizhu!=0:
				red.set_cookie('uname',uname)
			else:
				red.set_cookie('uname','',max_age=-1)
			#把用户名和ID加到session中，以便后面常用
			request.session['user_id']=users[0].id
			request.session['user_name']=uname
			return red
		else:
			context={'title':'登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
			return render(request,'df_user/login.html',context)
	else:
		context={'title': '登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
		return render(request,'df_user/login.html',context)

def info(request):
	user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
	print user_email
	context={'title':'用户中心','user_email':user_email,'user_name':request.session['user_name']}
	return render(request,'df_user/user_center_info.html',context)

def order(request):
	context={'title':'用户中心'}
	return render(request, 'df_user/user_center_order.html',context)
def site(request):
	#查到一个对像
	user=UserInfo.objects.get(id=request.session['user_id'])
	if request.method=='POST':
		post=request.POST
		user.ushou=post.get('ushou')
		user.uaddress = post.get('uaddress')
		user.uyoubian = post.get('uyoubian')
		user.uphone = post.get('uphone')
		user.save()
	context={'title':'用户中心','user':user}
	return render(request, 'df_user/user_center_site.html',context)