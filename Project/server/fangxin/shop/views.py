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

from shop.models import ShoppingCart
from shop.models import CartItem
from shop.models import RedPack
from shop.models import Order
from shop.models import OrderItem

from shop.models import GroupNorm

APP_ID = '1'
APP_SECRET = '2'

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
    appid = 'wx73bdc6a0b793aa42'
    secret = 'd18f4ce06504cc4d7c2dbb0e06e03929'
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
    		auth = User.objects.get(id=openid)
    		if not auth:
        		raise Unauthorized('wxapp_not_registered')
    		return auth
    	except User.DoesNotExist:
    		acc = User()
    		acc.id = openid
    		acc.nickname = nickname
    		acc.avatar = avatar
    		acc.created_time = datetime.now()
    		acc.updated_time = datetime.now()
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
        "sub": account.id,
        "nickname": account.nickname,
        "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    print('----------------------------')
    print(token)
    print(account.id)
    token = str(token, encoding="utf-8")
    resp = {'access_token': token, 'account_id': account.id}
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
		the_user = User.objects.get(id=client_account_id)
		print(the_user)
		res_dict = dict(nickName=the_user.nickname,avatarUrl=the_user.avatar,userDesc=the_user.user_des)
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

    

    res_dict = dict(today=todayProducts,hot=hotProducts,selected=selectedProducts)
    res_json = json.dumps(res_dict)
    return HttpResponse(res_json)
