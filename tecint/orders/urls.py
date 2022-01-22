# import libraries here 
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderStatusViewSet
from . import views

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_num),
    path('orders/items/', views.order_items),
    path('orders/items/<int:pk>/', views.item_num),
    path('order_status/', OrderStatusViewSet.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)