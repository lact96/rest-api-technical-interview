# import libraries here 
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderSeasonViewSet
from . import views

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('customer_order/', views.customer_order_list),
    path('order_seasons/', OrderSeasonViewSet.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)