#_*_coding:utf-8_*_
from django.shortcuts import render
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
    print 'typ01'
    return  render(request,'df_goods/index.html',context)

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
    return render(request,'df_goods/detail.html',context)

def base(request):
    return render(request,'df_goods/base.html')