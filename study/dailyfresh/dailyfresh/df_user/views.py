# _*_coding:utf-8_*_
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
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


