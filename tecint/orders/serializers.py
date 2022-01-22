#Serialization is the process of converting a Model to JSON.

#import libraries here
from rest_framework import serializers
from .models import OrderNumber, OrderLines, OrderStatus

#class method to specify what we wish to serialize the
class OrderNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderNumber
        fields = ['order_number']
class OrderLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLines
        fields = ('order_number', 'item_name', 'status')
    
class OrderStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderStatus
        fields = ('order', 'items', 'status')