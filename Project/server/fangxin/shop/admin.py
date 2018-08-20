from django.contrib import admin

from .models import Address
from .models import User
from .models import Shop
from .models import ShopBannar
from .models import AbstractType
from .models import ProductType
from .models import ShopProduct
from .models import ProductSpec
from .models import ProductGroup
from .models import ProductPicture
from .models import ShoppingCart
from .models import CartItem
from .models import RedPack
from .models import Deliver
from .models import Order
from .models import OrderItem
from .models import GroupUser

# Register your models here.


admin.site.register(Address)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(ShopBannar)
admin.site.register(ProductType)
admin.site.register(ShopProduct)
admin.site.register(ProductSpec)
admin.site.register(ProductGroup)
admin.site.register(ProductPicture)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(RedPack)
admin.site.register(Order)
admin.site.register(Deliver)
admin.site.register(OrderItem)
admin.site.register(GroupUser)

