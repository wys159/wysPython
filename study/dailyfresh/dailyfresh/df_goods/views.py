from django.shortcuts import render

def index(request):
    context={'page_cart':1}
    return  render(request,'df_goods/index.html',context)
