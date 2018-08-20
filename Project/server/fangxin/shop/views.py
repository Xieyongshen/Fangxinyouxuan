from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
import datetime
import jwt
import json
from django.core import serializers
from datetime import datetime
import time
import uuid
import random
import decimal
from math import sin, asin, cos, radians, fabs, sqrt
from shop.models import Address
from shop.models import User
from shop.models import Shop
from shop.models import ShopBannar
from shop.models import AbstractType
from shop.models import ProductType
from shop.models import ShopProduct
from shop.models import ProductSpec
from shop.models import ProductGroup
from shop.models import ProductPicture
from shop.models import ShoppingCart
from shop.models import CartItem
from shop.models import RedPack
from shop.models import Deliver
from shop.models import Order
from shop.models import OrderItem
from shop.models import GroupUser

# APP_ID = '1'
# APP_SECRET = '2'
APP_IMG_URL = 'http://119.23.225.244/uploads/'
# api = WXAPPAPI(appid=APP_ID,
#                   app_secret=APP_SECRET)
# session_info = api.exchange_code_for_session_key(code=code)

# # 获取session_info 后

# session_key = session_info.get('session_key')
# crypt = WXBizDataCrypt(WXAPP_APPID, session_key)

# # encrypted_data 包括敏感数据在内的完整用户信息的加密数据
# # iv 加密算法的初始向量
# # 这两个参数需要js获取
# user_info = crypt.decrypt(encrypted_data, iv)
# # Create your views here.

def get_wxapp_userinfo(encrypted_data, iv, code):
    from weixin.lib.wxcrypt import WXBizDataCrypt
    from weixin import WXAPPAPI
    from weixin.oauth2 import OAuth2AuthExchangeError
    appid = 'wx2e9255742bd9060a'
    secret = 'b36deef16567ff06be01673e590ccfcf'
    api = WXAPPAPI(appid=appid, app_secret=secret)
    try:
        # 使用 code  换取 session key    
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        raise Unauthorized(e.code, e.description)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(appid, session_key)
    # 解密得到 用户信息
    user_info = crypt.decrypt(encrypted_data, iv)
    print(user_info)
    return user_info


def verify_wxapp(encrypted_data, iv, code):
	# print('-------------')
	# print(code)
    user_info = get_wxapp_userinfo(encrypted_data, iv, code)
    # 获取 openid
    openid = user_info.get('openId', None)
    nickname = user_info.get('nickName', None)
    avatar = user_info.get('avatarUrl', None)
    print(openid)
    if openid:
    	try:
    		auth = User.objects.get(user_openid=openid)
    		if not auth:
        		raise Unauthorized('wxapp_not_registered')
    		return auth
    	except User.DoesNotExist:
    		acc = User()
    		acc.user_openid = openid
    		acc.user_name = nickname
    		acc.user_image = avatar
    		acc.create_time = datetime.now()
    		acc.save()
    	
    	raise Unauthorized('invalid_wxapp_code')
    
  
def create_token(request):
    # verify basic token
    approach = request.POST['auth_approach']
    username = request.POST['username']
    password = request.POST['password']
    print(approach)
    print(username)
    print(password)
    print(request.GET.get('code'))
    account = verify_wxapp(username, password, request.GET.get('code'))
    if not account:
        return False, {}
    payload = {
        "sub": account.user_openid,
        "nickname": account.user_name,
        "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    print('----------------------------')
    print(token)
    print(account.user_openid)
    token = str(token, encoding="utf-8")
    resp = {'access_token': token, 'account_id': account.user_openid}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def verify_token(token):
	try:
		payload = jwt.decode(token, 'secret', algorithm='HS256')
	except Exception as e:
		return False
	else:
		pass
	finally:
		pass
	
	if payload:
		return True, token
	return False, token

EARTH_RADIUS=6371           # 地球平均半径，6371km
 
def hav(theta):
    s = sin(theta / 2)
    return s * s
 
def get_distance_hav(lat0, lng0, lat1, lng1):
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
 
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
 
    return distance


def login(request):
	client_access_token = request.GET['access_token']
	client_account_id = request.GET['account_id']
	print(client_access_token)
	print(client_account_id)
	res_dict = dict()
	if(verify_token(client_access_token)):
		the_user = User.objects.get(user_openid=client_account_id)
		print(the_user)
		res_dict = dict(nickName=the_user.user_name,avatar=the_user.user_image)
	else:
		print('false')
	res_json = json.dumps(res_dict)
	return HttpResponse(res_json)

def getShops(request):
    res_dict = list()
    currentXstr = request.GET['currentX']
    currentYstr = request.GET['currentY']
    currentX = decimal.Decimal(currentXstr)
    currentY = decimal.Decimal(currentYstr)
    shopList = list(Shop.objects.all())
    for shops in shopList:
        d = round(1000 * get_distance_hav(currentX,currentY,shops.shop_X,shops.shop_Y),1)
        res_dict.append(dict(id=str(shops.shop_id),area=shops.shop_area,name=shops.shop_name,address=shops.shop_address,distance=d,shopKeeper=dict(name=shops.shop_man_name,phone=shops.shop_man_phone,avatar=shops.shop_man_avatar)))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getShopProduct(request):
    res_dict = dict()
    shopIdstr = request.GET['shopId']
    shopId = uuid.UUID(shopIdstr)
    the_shop = Shop.objects.get(shop_id=shopId)
    todayProducts = list()
    hotProducts = list()
    selectedProducts = list()
    shop_products = list(ShopProduct.objects.filter(shop__shop_id=shopId))
    
    for products in shop_products:
        if(products.activityType==1):
            todayEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.limitPrice),count=products.limitCount,remain=products.limitRemain,label=products.comment,limitStartTime=products.limitStartTime.strftime("%Y-%m-%d %H:%M:%S"),limitEndTime=products.limitEndTime.strftime("%Y-%m-%d %H:%M:%S"))
            todayProducts.append(todayEle)
    
    sortedPros = list(ShopProduct.objects.filter(shop__shop_id=shopId).order_by("buyTimes"))
    hotPros= sortedPros[-5:]
    returnHotPros = random.sample(hotPros, 3)
    for products in returnHotPros:
        if(products.activityType==1):
            hotEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.limitPrice),label=products.comment)
        elif(products.activityType==2):
            hotEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.groupPrice),label=products.comment)
        else:
            hotEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.pro_price),label=products.comment)
        hotProducts.append(hotEle)

    for products in shop_products:
        if(products.activityType==1):
            selectedEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.limitPrice),label=products.comment)
        elif(products.activityType==2):
            selectedEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.groupPrice),label=products.comment)
        else:
            selectedEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.pro_price),label=products.comment)
        selectedProducts.append(selectedEle)

    res_dict = dict(today=todayProducts,hot=hotProducts,selected=selectedProducts)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getShopCategory(request):
    res_dict = list()
    categories = list(ProductType.objects.filter(type_level=0))
    for category in categories:
        res_dict.append(dict(title=category.type_name,id=str(category.type_id),imgUrl=APP_IMG_URL+str(category.type_icon)))

    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getCategoryProduct(request):
    res_dict = dict()
    typeDict = list()
    productDict = list()
    shopIdstr = request.GET['shopId']
    categoryIdstr = request.GET['categoryId']
    shopId = uuid.UUID(shopIdstr)
    categoryId = uuid.UUID(categoryIdstr)
    typeList = list(ProductType.objects.filter(parent__type_id=categoryId))
    for types in typeList:
        typeEle = dict(id=str(types.type_id),name=types.type_name,imgUrl=APP_IMG_URL+str(types.type_icon))
        typeDict.append(typeEle)

    productList = list(ShopProduct.objects.filter(shop__shop_id=shopId,pro_type__parent__type_id=categoryId))
    for products in productList:
        productEle = dict(id=str(products.pro_id),type=str(products.pro_type.type_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.pro_price))
        productDict.append(productEle)

    res_dict = dict(type=typeDict,product=productDict)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getProductDetail(request):
    res_dict = dict()
    productIdstr = request.GET['productId']
    productId = uuid.UUID(productIdstr)
    the_product = ShopProduct.objects.get(pro_id=productId)
    if(the_product.activityType==2):
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=the_product.pro_id))
        imgUrls = list()
        imgUrls.append(dict(imgUrl=APP_IMG_URL+str(the_product.pro_image),type=0))
        for images in productPics:
            imgUrls.append(dict(imgUrl=APP_IMG_URL+str(images.url),url='',type=images.pictureType))
        recomendProList = list(ShopProduct.objects.filter(pro_type__type_id=the_product.pro_type.type_id))
        recomendList = list()
        for recPros in recomendProList:
            recomendList.append(dict(id=str(recPros.pro_id),name=recPros.pro_name,price=str(recPros.pro_price),imgUrl=APP_IMG_URL+str(recPros.pro_image)))
        productgroups = ProductGroup.objects.filter(group_product__pro_id=the_product.pro_id)
        groupList = list()
        for productgroup in productgroups:
            groupList.append(dict(head=dict(id=str(productgroup.groupuser_id),name=productgroup.group_monitor.user_name,avatar=productgroup.group_monitor.user_image),count=productgroup.group_number,reachCount=productgroup.group_maxNum,endTime=productgroup.end_time.strftime("%Y-%m-%d %H:%M:%S")))
        groupDetail = dict(price=str(the_product.groupPrice),list=groupList,count=len(groupList),reachCount=productgroups[0].group_maxNum)
        specList = list(ProductSpec.objects.filter(product__pro_id=the_product.pro_id))
        productSpec = list()
        for specs in specList:
            productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
        res_dict = dict(id=productIdstr,type=2,name=the_product.pro_name,desc=the_product.pro_desc,price=str(the_product.pro_price),groupPrice=str(the_product.groupPrice),oriPrice=str(the_product.pro_origin_price),soldCount=the_product.buyTimes,remain=the_product.pro_remain,detail=the_product.pro_detail,spec=productSpec,producer=the_product.pro_producer,image=imgUrls,group=groupDetail,recommend=recomendList,fullCount=the_product.fullCount,fullMinus=the_product.fullMinus)
    elif(the_product.activityType==1):
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=the_product.pro_id))
        imgUrls = list()
        imgUrls.append(dict(imgUrl=APP_IMG_URL+str(the_product.pro_image),type=0))
        for images in productPics:
            imgUrls.append(dict(imgUrl=APP_IMG_URL+str(images.url),url='',type=images.pictureType))
        recomendProList = list(ShopProduct.objects.filter(pro_type__type_id=the_product.pro_type.type_id))
        recomendList = list()
        for recPros in recomendProList:
            recomendList.append(dict(id=str(recPros.pro_id),name=recPros.pro_name,price=str(recPros.pro_price),imgUrl=APP_IMG_URL+str(recPros.pro_image)))
        specList = list(ProductSpec.objects.filter(product__pro_id=the_product.pro_id))
        productSpec = list()
        for specs in specList:
            productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
        res_dict = dict(id=productIdstr,type=the_product.activityType,name=the_product.pro_name,desc=the_product.pro_desc,price=str(the_product.pro_price),limitPrice=str(the_product.limitPrice),soldCount=the_product.buyTimes,remain=the_product.pro_remain,detail=the_product.pro_detail,spec=productSpec,producer=the_product.pro_producer,image=imgUrls,recommend=recomendList,limitStartTime=the_product.limitStartTime.strftime("%Y-%m-%d %H:%M:%S"),limitEndTime=the_product.limitEndTime.strftime("%Y-%m-%d %H:%M:%S"),fullCount=the_product.fullCount,fullMinus=the_product.fullMinus)
    
    elif(the_product.activityType==4):
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=the_product.pro_id))
        imgUrls = list()
        imgUrls.append(dict(imgUrl=APP_IMG_URL+str(the_product.pro_image),type=0))
        for images in productPics:
            imgUrls.append(dict(imgUrl=APP_IMG_URL+str(images.url),url='',type=images.pictureType))
        recomendProList = list(ShopProduct.objects.filter(pro_type__type_id=the_product.pro_type.type_id))
        recomendList = list()
        for recPros in recomendProList:
            recomendList.append(dict(id=str(recPros.pro_id),name=recPros.pro_name,price=str(recPros.pro_price),imgUrl=APP_IMG_URL+str(recPros.pro_image)))
        specList = list(ProductSpec.objects.filter(product__pro_id=the_product.pro_id))
        productSpec = list()
        for specs in specList:
            productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
        res_dict = dict(id=productIdstr,type=the_product.activityType,name=the_product.pro_name,desc=the_product.pro_desc,price=str(the_product.pro_price),soldCount=the_product.buyTimes,remain=the_product.pro_remain,detail=the_product.pro_detail,spec=productSpec,producer=the_product.pro_producer,image=imgUrls,recommend=recomendList,reachTime=the_product.reachTime.strftime("%Y-%m-%d %H:%M:%S"),fullCount=the_product.fullCount,fullMinus=the_product.fullMinus)
    else:
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=the_product.pro_id))
        imgUrls = list()
        imgUrls.append(dict(imgUrl=APP_IMG_URL+str(the_product.pro_image),type=0))
        for images in productPics:
            imgUrls.append(dict(imgUrl=APP_IMG_URL+str(images.url),url='',type=images.pictureType))
        recomendProList = list(ShopProduct.objects.filter(pro_type__type_id=the_product.pro_type.type_id))
        recomendList = list()
        for recPros in recomendProList:
            recomendList.append(dict(id=str(recPros.pro_id),name=recPros.pro_name,price=str(recPros.pro_price),imgUrl=APP_IMG_URL+str(recPros.pro_image)))
        specList = list(ProductSpec.objects.filter(product__pro_id=the_product.pro_id))
        productSpec = list()
        for specs in specList:
            productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
        res_dict = dict(id=productIdstr,type=the_product.activityType,name=the_product.pro_name,desc=the_product.pro_desc,price=str(the_product.pro_price),soldCount=the_product.buyTimes,remain=the_product.pro_remain,detail=the_product.pro_detail,spec=productSpec,producer=the_product.pro_producer,image=imgUrls,recommend=recomendList,fullCount=the_product.fullCount,fullMinus=the_product.fullMinus)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getOrderList(request):
    res_dict = list()
    client_access_token = request.GET['access_token']
    client_account_id = request.GET['account_id']
    if(verify_token(client_access_token)):
        the_user_orderList = list(Order.objects.filter(user__user_openid=client_account_id))
        for orders in the_user_orderList:
            if(orders.order_type==2):
                orderItems = list(OrderItem.objects.filter(order__order_id=orders.order_id))
                itemList = list()
                totalPrice = 0
                for items in orderItems:
                    totalPrice += items.product.pro_price*items.quantity
                    productgroup = ProductGroup.objects.get(group_product__pro_id=items.product.pro_id)
                    specList = list(ProductSpec.objects.filter(product__pro_id=items.product.pro_id))
                    productSpec = list()
                    for specs in specList:
                        productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
                    itemList.append(dict(id=str(items.product.pro_id),name=items.product.pro_name,imgUrl=APP_IMG_URL+str(items.product.pro_image),spec=productSpec,price=str(items.product.pro_price),oriPrice=str(items.product.pro_origin_price),count=items.quantity,people=productgroup.group_number,maxpeople=productgroup.group_maxNum))
                res_dict.append(dict(id=str(orders.order_id),status=orders.order_status,type=2,total=str(totalPrice),createTime=orders.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=orders.send_time.strftime("%Y-%m-%d"),product=itemList,orderNum=orders.order_num))
            else:
                orderItems = list(OrderItem.objects.filter(order__order_id=orders.order_id))
                itemList = list()
                totalPrice = 0
                for items in orderItems:
                    totalPrice += items.product.pro_price*items.quantity
                    specList = list(ProductSpec.objects.filter(product__pro_id=items.product.pro_id))
                    productSpec = list()
                    for specs in specList:
                        productSpec.append(dict(name=specs.spec_name,price=str(specs.spec_price)))
                    itemList.append(dict(id=str(items.product.pro_id),name=items.product.pro_name,imgUrl=APP_IMG_URL+str(items.product.pro_image),spec=productSpec,price=str(items.product.pro_price),oriPrice=str(items.product.pro_origin_price),count=items.quantity))
                res_dict.append(dict(id=str(orders.order_id),status=orders.order_status,type=orders.order_type,total=str(totalPrice),createTime=orders.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=orders.send_time.strftime("%Y-%m-%d"),product=itemList,orderNum=orders.order_num))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getOrderDetail(request):
    orderIdstr = request.GET['orderId']
    orderId = uuid.UUID(orderIdstr)
    the_order = Order.objects.get(order_id=orderId)
    if(the_order.order_type==2):
        orderItem = OrderItem.objects.get(order__order_id=the_order.order_id)
        totalPrice = orderItem.product.pro_price*orderItem.quantity
        totalOffer = orderItem.order_offer
        the_product = dict(id=str(orderItem.product.pro_id),name=orderItem.product.pro_name,imgUrl=APP_IMG_URL+str(orderItem.product.pro_image),price=str(orderItem.product.pro_price),oriPrice=str(orderItem.product.pro_origin_price),count=orderItem.quantity)
        productgroup = ProductGroup.objects.get(group_product__pro_id=orderItem.product.pro_id)
        the_group_users = list(GroupUser.objects.filter(productGroup__groupuser_id=productgroup.groupuser_id))
        user_infos = list()
        for users in the_group_users:
            user_infos.append(dict(id=users.user.user_openid,name=users.user.user_name,avatar=user.user.user_image))
        if(the_order.is_useRedPack):
            res_dict=dict(status=the_order.order_status,type=the_order.order_type,total=str(totalPrice),createTime=the_order.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=the_order.send_time.strftime("%Y-%m-%d"),discount=str(totalOffer),redPacket=str(the_order.order_redpack.red_amount),pay='在线支付',remark='',shop=dict(avatar=the_order.shop.shop_man_avatar,name=the_order.shop.shop_man_name,phone=the_order.shop.shop_man_phone),group = dict(count=productgroup.group_number,users=user_infos),product=the_product,orderNum=the_order.order_num)
        else:
            res_dict=dict(status=the_order.order_status,type=the_order.order_type,total=str(totalPrice),createTime=the_order.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=the_order.send_time.strftime("%Y-%m-%d"),discount=str(totalOffer),redPacket=str(0.00),pay='在线支付',remark='',shop=dict(avatar=the_order.shop.shop_man_avatar,name=the_order.shop.shop_man_name,phone=the_order.shop.shop_man_phone),group = dict(count=productgroup.group_number,users=user_infos),product=the_product,orderNum=the_order.order_num)
    else:
        orderItems = list(OrderItem.objects.filter(order__order_id=the_order.order_id))
        itemList = list()
        totalPrice = 0
        totalOffer = 0
        totalPacket = 0
        productList = list()
        for items in orderItems:
            totalPrice += items.product.pro_price*items.quantity
            totalOffer += items.order_offer
            productList.append(dict(id=str(items.product.pro_id),name=items.product.pro_name,imgUrl=APP_IMG_URL+str(items.product.pro_image),price=str(items.product.pro_price),oriPrice=str(items.product.pro_origin_price),count=items.quantity))
        if(the_order.is_useRedPack):
            res_dict=dict(status=the_order.order_status,type=the_order.order_type,total=str(totalPrice),createTime=the_order.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=the_order.send_time.strftime("%Y-%m-%d"),discount=str(totalOffer),redPacket=str(the_order.order_redpack.red_amount),pay='在线支付',remark='',shop=dict(avatar=the_order.shop.shop_man_avatar,name=the_order.shop.shop_man_name,phone=the_order.shop.shop_man_phone),product=productList,orderNum=the_order.order_num)
        else:
            res_dict=dict(status=the_order.order_status,type=the_order.order_type,total=str(totalPrice),createTime=the_order.create_time.strftime("%Y-%m-%d %H:%M:%S"),deliverTime=the_order.send_time.strftime("%Y-%m-%d"),discount=str(totalOffer),redPacket=str(0.00),pay='在线支付',remark='',shop=dict(avatar=the_order.shop.shop_man_avatar,name=the_order.shop.shop_man_name,phone=the_order.shop.shop_man_phone),product=productList,orderNum=the_order.order_num)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def submitOrder(request):
    data = json.loads(request.body)
    client_access_token = data['access_token']
    client_account_id = data['account_id']
    shopIdstr = data['shopId']
    redPacketIdStr = data['redPacket']
    shopId = uuid.UUID(shopIdstr)
    redPackId = uuid.UUID(redPacketIdStr)
    orderTypestr = data['type']
    orderType = int(orderTypestr)
    totalPaystr = data['total']
    totalPay = decimal.Decimal(totalPaystr)
    deliver = data['deliver']
    print(deliver)
    productList = data['product']
    if(verify_token(client_access_token)):
        the_user = User.objects.get(user_openid=client_account_id)
        the_shop = Shop.objects.get(shop_id=shopId)
        new_deliver = Deliver.objects.create(del_name=deliver['name'],del_freight=deliver['freight'])
        new_deliver.save()
        try:
            the_redPack = RedPack.objects.get(red_id=redPackId)
            the_redPack.is_used = True
            new_order = Order.objects.create(user=the_user,shop=the_shop,is_useRedPack=True,order_redpack=the_redPack,order_type=orderType,order_status=0,payment=totalPay,order_totalprice=totalPay,order_deliver=new_deliver,pay_time=datetime.now(),end_time=datetime.now(),send_time=datetime.now(),close_time=datetime.now(),create_time=datetime.now(),update_time=datetime.now(),order_comment='')
            new_order.save()
            for products in productList:
                the_product = ShopProduct.objects.get(pro_id=uuid.UUID(products['id']))
                new_order_item = OrderItem.objects.create(order=new_order,product=the_product,quantity=int(products['count']),totalPrice=decimal.Decimal(int(products['count'])*decimal.Decimal(products['price'])),create_time=datetime.now())
        except Exception as e:
            new_order = Order.objects.create(user=the_user,shop=the_shop,is_useRedPack=False,order_type=orderType,order_status=0,payment=totalPay,order_totalprice=totalPay,order_deliver=new_deliver,pay_time=datetime.now(),end_time=datetime.now(),send_time=datetime.now(),close_time=datetime.now(),create_time=datetime.now(),update_time=datetime.now(),order_comment='')
            new_order.save()
            for products in productList:
                the_product = ShopProduct.objects.get(pro_id=uuid.UUID(products['id']))
                new_order_item = OrderItem.objects.create(order=new_order,product=the_product,quantity=int(products['count']),totalPrice=decimal.Decimal(int(products['count'])*decimal.Decimal(products['price'])),create_time=datetime.now())
    return HttpResponse('ok')
        

def getShoppingCart(request):
    res_dict = list()
    client_access_token = request.GET['access_token']
    client_account_id = request.GET['account_id']
    if(verify_token(client_access_token)):
        theShoppingCart = ShoppingCart.objects.get(user__user_openid=client_account_id)
        cartItemList = list(CartItem.objects.filter(cart__cart_id=theShoppingCart.cart_id))
        for cartItems in cartItemList:
            res_dict.append(dict(id=str(cartItems.product.pro_id),name=cartItems.product.pro_name,imgUrl=APP_IMG_URL+str(cartItems.product.pro_image),price=str(cartItems.product.pro_price),oriPrice=str(cartItems.product.pro_origin_price),count=cartItems.pro_count))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getUserAddress(request):
    res_dict = list()
    client_access_token = request.GET['access_token']
    client_account_id = request.GET['account_id']
    if(verify_token(client_access_token)):
        userAddressList = list(Address.objects.filter(user__user_openid=client_account_id))
        for addresses in userAddressList:
            res_dict.append(dict(id=str(addresses.address_id),name=addresses.address_contact,phone=addresses.address_phone,desc=addresses.address_detail,region=dict(province=addresses.address_province,city=addresses.address_city,area=addresses.address_area),mail=addresses.address_mail))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getMyBalance(request):
    res_dict = dict()
    client_access_token = request.GET['access_token']
    client_account_id = request.GET['account_id']
    if(verify_token(client_access_token)):
        the_user = User.objects.get(user_openid=client_account_id)
        res_dict = dict(balance=str(the_user.user_remain))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getUserRedPacket(request):
    res_dict = list()
    client_access_token = request.GET['access_token']
    client_account_id = request.GET['account_id']
    if(verify_token(client_access_token)):
        userRedPacketList = list(RedPack.objects.filter(user__user_openid=client_account_id))
        for redPacks in userRedPacketList:
            res_dict.append(dict(id=str(redPacks.red_id),count=str(redPacks.red_amount),overdue=redPacks.red_overdue,is_used=redPacks.is_used,name=redPacks.red_name,satisfy=str(redPacks.red_satisfy),date=redPacks.red_date.strftime("%Y-%m-%d")))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getRecommendPros(request):
    res_dict = list()
    shopIdstr = request.GET['shopId']
    shopId = uuid.UUID(shopIdstr)
    sortedPros = list(ShopProduct.objects.filter(shop__shop_id=shopId).order_by("buyTimes"))
    hotPros= sortedPros[-5:]
    returnHotPros = random.sample(hotPros, 3)
    for products in returnHotPros:
        res_dict.append(dict(id=str(products.pro_id),name=products.pro_name,price=str(products.pro_price),imgUrl=APP_IMG_URL+str(products.pro_image)))
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getCouponProducts(request):
    res_dict = dict()
    shopIdstr = request.GET['shopId']
    shopId = uuid.UUID(shopIdstr)
    shop_products = list(ShopProduct.objects.filter(shop__shop_id=shopId))
    todayProducts = list()
    for products in shop_products:
        if(products.activityType==1):
            todayEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=APP_IMG_URL+str(products.pro_image),oriPrice=str(products.pro_origin_price),price=str(products.limitPrice),count=products.limitCount,remain=products.limitRemain,label=products.comment,limitStartTime=products.limitStartTime.strftime("%Y-%m-%d %H:%M:%S"),limitEndTime=products.limitEndTime.strftime("%Y-%m-%d %H:%M:%S"))
            todayProducts.append(todayEle)
    groupProducts = list()
    groupProductList = list(ShopProduct.objects.filter(activityType=2))
    for products in groupProductList:
        productgroups = ProductGroup.objects.filter(group_product__pro_id=products.pro_id)
        groupList = list()
        for productgroup in productgroups:
            groupList.append(dict(id=str(productgroup.group_monitor.user_openid),avatar=productgroup.group_monitor.user_image))
        groupProducts.append(dict(id=str(products.pro_id),name=products.pro_name,imgUrl=APP_IMG_URL+str(products.pro_image),price=str(products.groupPrice),oriPrice=str(products.pro_origin_price),soldCount=products.buyTimes,buyer=groupList))
    res_dict = dict(limitProducts=todayProducts,groupProducts=groupProducts)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)

def getHotSearch(request):
	res_list = list()
	sortedPros = list(ShopProduct.objects.order_by("searchTime"))
	hotPros = sortedPros[-5:]
	returnPros = random.sample(hotPros, 3)
	for pros in returnPros:
		res_list.append(dict(id=str(pros.pro_id),name=pros.pro_name))
	res_json = json.dumps(res_list)
	return HttpResponse(res_json)

def getSearchResult(request):
	searchValue = request.GET['searchValue']
	res_dict = list()
	match_categories = set(ProductType.objects.filter(type_name__icontains=searchValue))
	match_products = set(ShopProduct.objects.filter(pro_name__icontains=searchValue))

	for products in match_products:
		products.searchTime = products.searchTime + 1
		products.save()
		eve_dict = dict(name=products.pro_name,id=str(products.pro_id),imgUrl=APP_IMG_URL+str(products.pro_image),price=str(products.pro_price),desc=products.pro_desc)
		res_dict.append(eve_dict)
	res_json = json.dumps(res_dict)
	return HttpResponse(res_json)