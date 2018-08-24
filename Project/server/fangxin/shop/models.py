from django.db import models
from django.conf import settings
from datetime import datetime
import uuid
import random
# Create your models here.

class User(models.Model):
	user_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	user_name = models.TextField(u'用户名称')
	user_image = models.TextField(u'用户头像')
	user_openid = models.TextField(default='unknown user')
	user_remain = models.DecimalField(u'用户余额',blank=True,null=True,max_digits=10, decimal_places=2)
	create_time = models.DateTimeField(u'创建时间',blank=True,default=datetime.now())

	def __str__(self):
		return self.user_name

class Address(models.Model):
	address_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	address_contact = models.TextField(u'联系人',blank=True, null=True,)
	address_phone = models.TextField(u'联系电话',blank=True, null=True,)
	address_province = models.TextField(u'省份',blank=True, null=True,)
	address_city = models.TextField(u'城市',blank=True, null=True,)
	address_area = models.TextField(u'地区',blank=True, null=True,)
	address_detail = models.TextField(u'详细住址',blank=True, null=True,)
	address_mail = models.TextField(u'邮箱',blank=True, null=True,)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	def __str__(self):
		return self.address_detail


class Shop(models.Model):
	shop_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	shop_name = models.TextField(u'商店名称')
	shop_area = models.TextField(u'商店地区')
	shop_address = models.TextField(u'商店地址',blank=True,null=True)
	shop_man_name = models.TextField(u'店长名称',blank=True,null=True)
	shop_man_phone = models.TextField(u'店长电话',blank=True,null=True)
	shop_man_avatar = models.TextField(u'店长头像',blank=True,null=True)
	shop_X = models.DecimalField(u'纬度',blank=True, null=True,max_digits=10, decimal_places=7)
	shop_Y = models.DecimalField(u'经度',blank=True, null=True,max_digits=10, decimal_places=7)

	def __str__(self):
		return self.shop_name

class AbstractType(models.Model):  
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)  
    class Meta:  
        abstract = True

class ProductType(AbstractType):
	type_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	type_name = models.TextField(u'商品类型名称')
	type_level = models.IntegerField(u'商品类型层级',default=0)
	type_icon = models.ImageField(u'分类图标',upload_to='img/%Y/%m/%d',null=True,blank=True)

	def __str__(self):
		return self.type_name

class ShopBannar(models.Model):
	bannar_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	bannar_url = models.ImageField(u'商店海报',upload_to='img/%Y/%m/%d',null=True,blank=True)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	position = models.IntegerField(u'布局位置',blank=True,null=True)
	banner_type = models.ForeignKey(ProductType,blank=True,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.bannar_url)

class ShopProduct(models.Model):
	pro_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	pro_name = models.TextField(u'商品名称')
	shop = models.ManyToManyField(Shop)
	pro_price = models.DecimalField(u'商品价格',max_digits=10, decimal_places=2)
	pro_origin_price = models.DecimalField(u'商品原价',blank=True, null=True,max_digits=10, decimal_places=2)
	pro_remain = models.IntegerField(u'商品库存')
	pro_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	pro_desc = models.TextField(u'商品描述',blank=True, null=True,)
	pro_detail = models.TextField(u'商品详情描述',blank=True, null=True,)
	pro_norm = models.TextField(u'商品规格',blank=True, null=True,)
	pro_producer = models.TextField(u'商品产地',blank=True, null=True,)
	on_shelf = models.BooleanField(u'是否上架')
	pro_image = models.ImageField(u'商品封面图',upload_to='img/%Y/%m/%d',null=True,blank=True)
	activityType = models.IntegerField(u'活动类型',blank=True, null=True)
	limitCount = models.IntegerField(u'限时商品总量',blank=True, null=True)
	limitRemain = models.IntegerField(u'限时商品剩余量',blank=True, null=True)
	limitStartTime = models.DateTimeField(u'限时商品开始时间',null=True, blank=True)
	limitEndTime = models.DateTimeField(u'限时商品截止时间',null=True, blank=True)
	limitPrice = models.DecimalField(u'限时商品优惠价',blank=True,null=True,max_digits=10, decimal_places=2)
	groupPrice = models.DecimalField(u'拼团商品优惠价',blank=True,null=True,max_digits=10, decimal_places=2)
	fullCount = models.DecimalField(u'满减商品满价',blank=True, null=True, max_digits=10, decimal_places=2)
	fullMinus = models.DecimalField(u'满减商品减价',blank=True, null=True, max_digits=10, decimal_places=2)
	reachTime = models.DateTimeField(u'预售商品到达时间', blank=True, null=True)
	comment = models.TextField(u'活动商品说明',blank=True, null=True)
	buyTimes = models.IntegerField(u'商品购买次数',default=0)
	searchTimes = models.IntegerField(u'搜索次数',default=0)

	def __str__(self):
		return self.pro_name

class ProductSpec(models.Model):
	spec_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	spec_name = models.TextField()
	spec_price = models.DecimalField(max_digits=10, decimal_places=2)
	product = models.ForeignKey(ShopProduct,on_delete=models.CASCADE)

	def __str__(self):
		return self.spec_name

class ProductGroup(models.Model):
	groupuser_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	group_monitor = models.ForeignKey(User, on_delete=models.CASCADE)
	group_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	group_code = models.TextField(u'编号')
	group_number = models.IntegerField(u'参团人数')
	group_maxNum = models.IntegerField(u'团最大人数',default=10)
	create_time = models.DateTimeField(u'创建时间')
	end_time = models.DateTimeField(u'截止时间')
	group_status = models.IntegerField(u'团的状态')

	def __str__(self):
		return self.group_code

class GroupUser(models.Model):
	groupUsers_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	productGroup = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductPicture(models.Model):
	pic_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	shop_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	url = models.ImageField(u'商品图片',upload_to='img/%Y/%m/%d',null=True,blank=True)
	pictureType = models.IntegerField(u'图片类型',default=0)

	def __str__(self):
		return str(self.url)

class ShoppingCart(models.Model):
	cart_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	update_time = models.DateTimeField(u'更新时间',blank=True, null=True,)

	def __str__(self):
		return self.user.user_name

class CartItem(models.Model):
	cartItem_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	pro_count = models.IntegerField(u'商品数量')
	pro_price = models.IntegerField(u'商品价格')
	create_time = models.DateTimeField(u'创建时间')
	def __str__(self):
		return self.product.pro_name


class RedPack(models.Model):
	red_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	red_amount = models.DecimalField(u'红包数额',max_digits=10, decimal_places=2)
	red_name = models.TextField(u'名称',default='放心优选全场红包')
	red_type = models.IntegerField(u'红包类型',default=0)
	red_overdue = models.BooleanField(u'是否过期',default=False)
	red_satisfy = models.DecimalField(u'门槛数额',max_digits=10, decimal_places=2,default=0)
	red_date = models.DateTimeField(u'到期时间',null=True,blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_used = models.BooleanField(u'是否被用了')
	
	def __str__(self):
		return str(self.red_amount) + str(self.red_name)

class Deliver(models.Model):
	del_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	del_name = models.TextField()
	del_freight = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return str(self.del_name)

class Order(models.Model):
	order_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	order_num = models.TextField(u'订单编号',default=datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(10,99)))
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order_type = models.IntegerField(u'订单类型',default=0)
	order_status = models.IntegerField(u'订单状态')
	order_totalprice = models.DecimalField(u'订单总额',max_digits=10, decimal_places=2)
	order_deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE, blank=True, null=True)
	payment = models.DecimalField(u'已付金额',max_digits=10, decimal_places=2)
	pay_time = models.DateTimeField(u'付款时间')
	end_time = models.DateTimeField(u'付款结束时间')
	send_time = models.DateTimeField(u'发货时间')
	close_time = models.DateTimeField(u'交易关闭时间')
	create_time = models.DateTimeField(u'订单创建时间')
	update_time = models.DateTimeField(u'订单更新时间')
	order_comment = models.TextField(u'订单说明')
	is_useRedPack = models.NullBooleanField(u'是否用了红包')
	order_redpack = models.ForeignKey(RedPack, on_delete=models.CASCADE, blank=True, null=True)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.order_num

class OrderItem(models.Model):
	orderitem_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	order_offer = models.DecimalField(u'订单优惠',max_digits=10, decimal_places=2, default=0)
	quantity = models.IntegerField(u'商品数量')
	totalPrice = models.DecimalField(u'订单项总额',max_digits=10, decimal_places=2)
	create_time = models.DateTimeField(u'创建时间')

	def __str__(self):
		return self.product.pro_name
