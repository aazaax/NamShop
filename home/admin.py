from django.contrib import admin

# Register your models here.
from.models import Product,Category,User,Bill
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Bill)
admin.site.register(Category)