from django.contrib import admin

from .models import Address
from .models import User
from .models import Shop
from .models import ShopBannar
from .models import AbstractType
from .models import ProductType
from .models import ShopProduct
from .models import GroupProduct
from .models import ProductGroup
from .models import ShopProductPicture
from .models import GroupProductPicture
from .models import ShoppingCart
from .models import CartItem_ShopProduct
from .models import CartItem_GroupProduct
from .models import RedPack
from .models import Order
from .models import OrderItem_ShopProduct
from .models import OrderItem_GroupProduct
from .models import GroupNorm
# Register your models here.


admin.site.register(Address)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(ShopBannar)
admin.site.register(ProductType)
admin.site.register(ShopProduct)
admin.site.register(GroupProduct)
admin.site.register(ProductGroup)
admin.site.register(ShopProductPicture)
admin.site.register(GroupProductPicture)
admin.site.register(ShoppingCart)
admin.site.register(CartItem_ShopProduct)
admin.site.register(CartItem_GroupProduct)
admin.site.register(RedPack)
admin.site.register(Order)
admin.site.register(OrderItem_ShopProduct)
admin.site.register(OrderItem_GroupProduct)
admin.site.register(GroupNorm)
