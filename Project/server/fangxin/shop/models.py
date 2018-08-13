from django.db import models
from django.conf import settings
from datetime import datetime
import uuid
# Create your models here.

class User(models.Model):
	user_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	user_name = models.TextField()
	user_image = models.TextField()
	#user_address = models.ForeignKey(Address, on_delete=models.CASCADE)
	user_openid = models.TextField(default='unknown user')
	create_time = models.DateTimeField(blank=True,default=datetime.now())

	def __str__(self):
		return self.user_name

class Address(models.Model):
	address_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	address_contact = models.TextField(blank=True, null=True,)
	address_phone = models.TextField(blank=True, null=True,)
	address_area = models.TextField(blank=True, null=True,)
	address_detail = models.TextField(blank=True, null=True,)
	address_mail = models.TextField(blank=True, null=True,)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	def __str__(self):
		return self.address_detail


class Shop(models.Model):
	shop_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	shop_name = models.TextField()
	shop_area = models.TextField()
	shop_man_name = models.TextField(blank=True,null=True)
	shop_man_phone = models.TextField(blank=True,null=True)
	shop_man_avatar = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.shop_name

class ShopBannar(models.Model):
	bannar_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	bannar_url = models.TextField()
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

	def __str__(self):
		return self.bannar_url

class AbstractType(models.Model):  
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)  
    class Meta:  
        abstract = True

class ProductType(AbstractType):
	type_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	type_name = models.TextField()
	type_level = models.IntegerField(default=0)

	def __str__(self):
		return self.type_name

class ShopProduct(models.Model):
	pro_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	pro_name = models.TextField()
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	pro_price = models.DecimalField(max_digits=10, decimal_places=2)
	pro_origin_price = models.DecimalField(blank=True, null=True,max_digits=10, decimal_places=2)
	pro_remain = models.IntegerField()
	pro_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	pro_desc = models.TextField(blank=True, null=True,)
	pro_spec = models.TextField(blank=True, null=True,)
	pro_weight = models.TextField(blank=True, null=True,)
	pro_package = models.TextField(blank=True, null=True,)
	pro_life = models.TextField(blank=True, null=True,)
	pro_store_method = models.TextField(blank=True, null=True,)
	on_shelf = models.BooleanField()
	can_group = models.NullBooleanField(blank=True)
	activityType = models.IntegerField(blank=True, null=True)
	count = models.IntegerField(blank=True, null=True)
	remain = models.IntegerField(blank=True, null=True)
	group_price = models.DecimalField(default=0,max_digits=10, decimal_places=2)
	fullCount = models.IntegerField(blank=True, null=True)
	fullMinus = models.IntegerField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	buyTimes = models.IntegerField(default=0)
	def __str__(self):
		return self.pro_name

class GroupProduct(models.Model):
	pro_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, blank=True, null=True)
	comment = models.TextField(default='可拼团')
	def __str__(self):
		return self.product.pro_name

class limitTimeSale(models.Model):
	limit_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, blank=True, null=True)
	count = models.IntegerField()
	remain = models.IntegerField()
	comment = models.TextField(default="限时出售")

class Discount(models.Model):
	dis_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	count = models.IntegerField()
	minus = models.IntegerField()
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	comment = models.TextField(default='满50减20')

	def __str__(self):
		return self.product.pro_name

class ProductGroup(models.Model):
	groupuser_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	group_monitor = models.ForeignKey(User, on_delete=models.CASCADE)
	group_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	group_code = models.TextField()
	group_number = models.IntegerField()
	group_maxNum = models.IntegerField(default=10)
	create_time = models.DateTimeField()
	end_time = models.DateTimeField()
	group_status = models.IntegerField()

	def __str__(self):
		return self.group_code

class GroupUser(models.Model):
	groupUsers_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	productGroup = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductPicture(models.Model):
	pic_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	shop_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	url = models.TextField()

	def __str__(self):
		return self.url

class ShoppingCart(models.Model):
	cart_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	update_time = models.DateTimeField(blank=True, null=True,)

	def __str__(self):
		return self.user.user_name

class CartItem(models.Model):
	cartItem_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	pro_count = models.IntegerField()
	pro_price = models.IntegerField()
	is_checked = models.BooleanField()
	create_time = models.DateTimeField()

	def __str__(self):
		return self.product.pro_name


class RedPack(models.Model):
	red_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	red_amount = models.DecimalField(max_digits=10, decimal_places=2)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_used = models.BooleanField()

	def __str__(self):
		return str(self.red_amount)

class Order(models.Model):
	order_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	order_num = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order_status = models.IntegerField()
	order_totalprice = models.DecimalField(max_digits=10, decimal_places=2)
	payment = models.DecimalField(max_digits=10, decimal_places=2)
	pay_time = models.DateTimeField()
	end_time = models.DateTimeField()
	send_time = models.DateTimeField()
	close_time = models.DateTimeField()
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()
	order_comment = models.TextField()
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.order_num

class OrderItem(models.Model):
	orderitem_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
	order_redpack = models.ForeignKey(RedPack, on_delete=models.CASCADE, blank=True, null=True)
	order_offer = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	quantity = models.IntegerField()
	totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
	create_time = models.DateTimeField()

	def __str__(self):
		return self.product.pro_name


class GroupNorm(models.Model):
	norm_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4,editable=False)
	norm_name = models.TextField()
	norm_size = models.IntegerField()

	def __str__(self):
		return self.norm_name