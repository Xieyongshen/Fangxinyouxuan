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
from shop.models import Address
from shop.models import User
from shop.models import Shop
from shop.models import ShopBannar
from shop.models import AbstractType
from shop.models import ProductType
from shop.models import ShopProduct

from shop.models import ProductGroup
from shop.models import ProductPicture
from shop.models import limitTimeSale
from shop.models import ShoppingCart
from shop.models import CartItem
from shop.models import RedPack
from shop.models import Order
from shop.models import OrderItem
from shop.models import Discount
from shop.models import GroupNorm

# APP_ID = '1'
# APP_SECRET = '2'

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
            productPics = list(ProductPicture.objects.filter(shop_product__pro_id=products.pro_id))
            # imgUrl = productPics[0].url
            imgUrl = ''
            todayEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=imgUrl,oriPrice=str(products.pro_origin_price),price=str(products.pro_price),count=products.count,remain=products.remain,label=products.comment)
            todayProducts.append(todayEle)
    
    sortedPros = list(ShopProduct.objects.order_by("buyTimes"))
    hotPros= sortedPros[-5:]
    returnHotPros = random.sample(hotPros, 3)
    for products in returnHotPros:
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=products.pro_id))
        # imgUrl = productPics[0].url
        imgUrl = ''
        hotEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=imgUrl,oriPrice=str(products.pro_origin_price),price=str(products.pro_price),label=products.comment)
        hotProducts.append(hotEle)

    for products in shop_products:
        productPics = list(ProductPicture.objects.filter(shop_product__pro_id=products.pro_id))
        # imgUrl = productPics[0].url
        imgUrl = ''
        selectedEle = dict(id=str(products.pro_id),name=products.pro_name,desc=products.pro_desc,imgUrl=imgUrl,oriPrice=str(products.pro_origin_price),price=str(products.pro_price),label=products.comment)
        selectedProducts.append(selectedEle)

    res_dict = dict(today=todayProducts,hot=hotProducts,selected=selectedProducts)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)
