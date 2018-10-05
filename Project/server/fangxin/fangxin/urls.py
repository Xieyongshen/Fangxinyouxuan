"""fangxin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from shop import views as fangxin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/token', fangxin_views.create_token, name='token'),
    path('api/login', fangxin_views.login),
    path('api/getShops', fangxin_views.getShops),
    path('api/getShopCategory', fangxin_views.getShopCategory),
    path('api/getShopProduct', fangxin_views.getShopProduct),
    path('api/getCategoryProduct', fangxin_views.getCategoryProduct),
    path('api/getProductDetail', fangxin_views.getProductDetail),
    path('api/getOrderList', fangxin_views.getOrderList),
    path('api/getOrderDetail', fangxin_views.getOrderDetail),
    path('api/getShoppingCart', fangxin_views.getShoppingCart),
    path('api/getUserAddress', fangxin_views.getUserAddress),
    path('api/getMyBalance', fangxin_views.getMyBalance),
    path('api/getUserRedPacket', fangxin_views.getUserRedPacket),
    path('api/getRecommendPros', fangxin_views.getRecommendPros),
    path('api/getCouponProducts', fangxin_views.getCouponProducts),
    path('api/submitOrder', fangxin_views.submitOrder),
    path('api/getHotSearch', fangxin_views.getHotSearch),
    path('api/getSearchResult', fangxin_views.getSearchResult),
    path('api/saveMyAddress', fangxin_views.saveMyAddress),
    path('api/deleteMyAddress', fangxin_views.deleteMyAddress),
    path('api/getBanners', fangxin_views.getBanners),
    path('api/getCategoryBanners', fangxin_views.getCategoryBanners),
    path('api/getToken', fangxin_views.getToken),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
