#_*_coding:utf-8_*_
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from models import *
def index(request):

    typelist=TypeInfo.objects.all()
    #查询各分类取最新4条与最热4条
    type0=typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context={'title':'首页','page_cart':1,
             'type0':type0,'type01':type01,
             'type1': type1, 'type11': type11,
             'type2': type2, 'type21': type21,
             'type3': type3, 'type31': type31,
             'type4': type4, 'type41': type41,
             'type5': type5, 'type51': type51,
             }
    # 把当前访问的页面存入到cookies中以便以后用到
    # response=render_to_response(request,'df_goods/index.html',context, context_instance = RequestContext(request))
    # response.set_cookie('url',request.get_full_path())
    # return response
    # url = request.COOKIES.get('url')
    #
    # if request.get_full_path()!=url and request.get_full_path() is not None:
    #     red=HttpResponseRedirect(url)
    #     red.set_cookie('url',request.get_full_path())
    # response= render(request,'df_goods/index.html',context)
    # response.set_cookie('url',request.get_full_path())
    # return  response
    return render(request, 'df_goods/index.html', context)

def list(request,tid,pindex,sort):
    #tid当前商品类型 ，pindex当前页码,sort按什么排序
    typeinfo=TypeInfo.objects.get(pk=int(tid))#查到当前id对应的类型
    news=typeinfo.goodsinfo_set.order_by('-id')[0:2]#查到当前类型最新商品
    if sort=='1':#默认排序 最新的
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':#价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gpric')
    elif sort == '3':#人气，点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    #分页
    paginator=Paginator(goods_list,10)
    page=paginator.page(int(pindex))
    context={'title':typeinfo.ttitle,'page_cart':1,
             'page':page,
             'paginator':paginator,
             'typeinfo':typeinfo,
             'sort':sort,
             'news':news
             }

    return render(request,'df_goods/list.html',context)

def detail(request,id):
    goods=GoodsInfo.objects.get(pk=int(id))
    # 维护人气字段gclick
    goods.gclick=goods.gclick+1
    goods.save()
    #最新的新品
    news=goods.gtype.goodsinfo_set.order_by('-id')[0:2]

    context={'title':goods.gtype.ttitle,'page_cart':1,
             'goods':goods,
             'typeinfo':goods.gtype,
             'news':news,'id':id
             }

    response=render(request,'df_goods/detail.html',context)

    #记录最近浏览，在用户中心显示
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_id='%d'%goods.id
    if goods_ids!='':#判断是否有浏览记录，如果有则继续判断
        goods_ids1=goods_ids.split(',')#把cookies中的记录拆分成列表
        if goods_ids1.count(goods_id)>=1:#若记录已存在，则删除
            goods_ids1.remover(goods_id)
        goods_ids1.insert(0,goods_id)#再把记录填加到第一个
        if len(goods_ids1)>=6:#若超过6个则把最后一个删除
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)#拼接字符串
    else:
        goods_ids=goods_id
    response.set_cookie('goods_ids',goods_ids)#写入到cookie中

    return response

def base(request):
    return render(request,'df_goods/base.html')