# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item
class ComSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    spurl = Field()
    spname = Field()
    spmaijia = Field()
    sppl = Field()
    spplriqi = Field()
    sp_brand = Field()
    sp_models = Field()
class AvccollectionagentItem(Item):
    #  url, 商品名称，买家，评论，评论日期，
    sp_url = Field()
    sp_name = Field()
    sp_maijia = Field()
    sp_pl = Field()
    sp_plriqi = Field()
    #  品牌，商品型号，店铺，网页价格，评论指数，评论中型号，促销价格
    sp_brand = Field()
    sp_models = Field()
    sp_dianp = Field()
    sp_web_price = Field()
    sp_score = Field()
    productColor = Field()
    cx_price = Field()
    color = Field()

    sp_leibie = Field()
    sp_gmnum = Field()
    url_web = Field()
    replies = Field()
    official_reply = Field()
    attr = Field()
    cx_info = Field()

# 天猫月销量
class TmSellCountItem(Item):
    # 商品名称,评论日期,单价,月销量,页面信息,品牌,机型,旗舰店,评论
    spurl = Field()
    collectiontime = Field()
    shopname = Field()
    skuid = Field()
    yanseid = Field()
    typeid = Field()
    yansename = Field()
    typename = Field()
    webprice = Field()
    price = Field()
    sellcount = Field()  # 月销量
    quantity = Field()  # 库存
# 电商URL
class EcUrlItem(Item):
    platform = Field()
    url = Field()
    price = Field()
    brand = Field()
    category = Field()
    collectiontime = Field()
# 电商评论&回复 采集 items
class EcplReplyItem(Item):
    url = Field()
    platform = Field()
    category = Field()
    brand = Field()
    model = Field()
    commentContent = Field()
    commentType = Field()
    buyerName = Field()
    commentTime = Field()
    replyContent = Field()
    replyer = Field()
    replyTime = Field()
    shopname = Field()
    commentStates = Field()
# 京东项目 URL采集 items
class JdAttributeUrlItem(Item):
    url = Field()
    platform = Field()
    skuId = Field()
    catId = Field()
    category1 = Field()
    collectiontime = Field()
# 京东项目 属性采集
class JdAttributeItem(Item):
    platform = Field()
    spuId = Field()
    spName = Field()
    skuId = Field()
    url = Field()
    brandId = Field()
    brand = Field()
    catId = Field()
    catName = Field()
    shopName = Field()
    shopId = Field()
    tagPrice = Field()
    promoPrice = Field()
    cxMsg = Field()
    maizeng = Field()
    # fanquan = Field()
    rangli = Field()
    tuangou = Field()
    jifen = Field()
    dazhe = Field()
    reviewsCount = Field()
    godsRank = Field()
    dealCount = Field()
    collectiontime = Field()
    attributelist = Field(serializer=dict)
