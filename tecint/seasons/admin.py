from django.contrib import admin
from .models import CustomerOrders, OrderSeason
# Register your models here.
admin.site.register(CustomerOrders)
admin.site.register(OrderSeason)