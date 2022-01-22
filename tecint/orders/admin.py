from django.contrib import admin
from .models import OrderNumber, OrderLines, OrderStatus
# Register your models here.


# Class method will update the admine site to have the many-to-many relation horizontal

    
#register models to the admin interface
admin.site.register(OrderNumber)
admin.site.register(OrderLines)
class OrderStatusAdmin(admin.ModelAdmin):
    filter_horizontal = "items",
admin.site.register(OrderStatus, OrderStatusAdmin)