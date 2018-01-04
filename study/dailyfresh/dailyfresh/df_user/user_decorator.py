#_*_coding:utf-8_*_

from django.http import HttpResponseRedirect

#如查未登录转到登录页面
def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red=HttpResponseRedirect('/user/login/')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun

'''
http://127.0.0.1:8000/200/?type=10
request.path: 表示当前路径:返回值为/200

request.get_full_path():表示完整路径 返回值为/200/？type=10
'''