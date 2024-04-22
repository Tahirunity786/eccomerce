from django.contrib import admin
from core_control.models import Product, ProductImages, Address, Orders
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Address)
admin.site.register(Orders)
