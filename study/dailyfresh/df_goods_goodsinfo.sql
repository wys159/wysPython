/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.0.51b-community-nt-log 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `df_goods_goodsinfo` (
	`id` int (11),
	`gtitle` varchar (60),
	`gpic` varchar (300),
	`gpric` Decimal (7),
	`isDelete` tinyint (1),
	`gunit` varchar (60),
	`gclick` int (11),
	`gjianjie` varchar (600),
	`gcontent` text ,
	`gkucun` int (11),
	`gtype_id` int (11)
); 
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('1','越南进口红心火龙果 2个装 大果 单果约','df_goods/goods004.jpg','39.90','0','','22','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('2','五丰 美仑达 精品琯溪蜜柚 红心柚子2个','df_goods/goods004.jpg','39.90','0','','12','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('3','五丰 美仑达 精品琯溪 ','df_goods/goods004.jpg','39.90','0','','12','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('4','仑达 精品琯溪蜜柚 红心柚子2个装 2k','df_goods/goods004.jpg','39.90','0','','66','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('5','仑达 精品琯溪蜜柚 ','df_goods/goods004.jpg','39.90','0','','66','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('6','2个装 大果 单果约450~500g 新','df_goods/goods004.jpg','39.90','0','','22','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('7','越南赣南脐橙 12粒铂金果 20新','df_goods/goods004.jpg','39.90','0','','8','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('8','五丰 美仑达 ','df_goods/goods004.jpg','39.90','0','','20','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('9','赣赣南脐橙 12粒铂金果 2017新果','df_goods/goods004.jpg','39.90','0','','6','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('10','越南赣南脐橙 12粒铂金果 20新','df_goods/goods004.jpg','39.90','0','','8','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('11','越南进口红心赣南脐橙 12粒铂金果 ','df_goods/goods004.jpg','39.90','0','','62','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('12','越南进口红心火龙果 2个装 大果 ','df_goods/goods004.jpg','39.90','0','','36','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('13','越南进口红心火龙果 2个装 大果 ','df_goods/goods004.jpg','39.90','0','','78','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('14','越南进口红心火龙果 2个装 大果 单果约','df_goods/goods004.jpg','39.90','0','','53','京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。\n注：本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。','折扣：如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。','55','1');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('15','冷冻翡翠生虾仁 200g 31-40只 ','df_goods/goods004.jpg','23.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('16','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('17','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('18','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','9','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('19','三都港 冷冻无公害黄花鱼 700g ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('20','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('21','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('22','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','22','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('23','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('24','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('25','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','85','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('26','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','360','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('27','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','45','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('28','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','88','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('29','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','2');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('30','冷冻翡翠生虾仁 200g 31-40只 ','df_goods/goods004.jpg','23.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('31','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('32','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('33','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','9','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('34','三都港 冷冻无公害黄花鱼 700g ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('35','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('36','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('37','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','22','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('38','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('39','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('40','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','85','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','23');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('41','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','360','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('42','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','45','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('43','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','88','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('44','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','3');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('45','冷冻翡翠生虾仁 200g 31-40只 ','df_goods/goods004.jpg','23.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('46','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('47','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('48','国联(GUO LIAN) 冷冻翡翠生虾仁','df_goods/goods004.jpg','118.00','0','','9','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('49','三都港 冷冻无公害黄花鱼 700g ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('50','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('51','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('52','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','22','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('53','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('54','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','4');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('55','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','85','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','5');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('56','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','360','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','5');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('57','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','45','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','5');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('58','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','88','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','5');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('59','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','5');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('60','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','22','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('61','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','8','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('62','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','2','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('63','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','85','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('64','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','360','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('65','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','45','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('66','獐子岛 冷冻大连蒜蓉粉丝 ','df_goods/goods004.jpg','118.00','0','','88','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');
insert into `df_goods_goodsinfo` (`id`, `gtitle`, `gpic`, `gpric`, `isDelete`, `gunit`, `gclick`, `gjianjie`, `gcontent`, `gkucun`, `gtype_id`) values('67','禧美(Seamix) 原装进口冷冻厄瓜 ','df_goods/goods004.jpg','118.00','0','','99','商品名称：GUO LIAN翡翠生虾仁71-90商品编号：2818537商品毛重：260.00g商品产地：中国广东保存状态：冷冻','注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，京东生鲜不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若京东生鲜没有及时更新，请大家谅解！','55','6');