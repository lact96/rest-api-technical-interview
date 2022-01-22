#Serialization is the process of converting a Model to JSON.

#import libraries here
from rest_framework import serializers
from .models import CustomerOrders, OrderSeason

#class method to specify what we wish to serialize
class CustomerOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrders
        fields = ['order_id', 'order_date', 'quantity_ordered']
class OrderSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSeason
        fields = ('order_id', 'season')