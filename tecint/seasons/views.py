from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import serializers
from .serializers import CustomerOrdersSerializer, OrderSeasonSerializer
#import Models
from .models import CustomerOrders, OrderSeason
from rest_framework.generics import(
    ListCreateAPIView
)
from datetime import date

# Create your views here.
#This function will create a new order and an order status:
@api_view(['GET', 'POST'])
def customer_order_list(request, format=None):
    #Handles get requests for viewing Order Numbers
    if request.method == 'GET':
        order = CustomerOrders.objects.all()
        serializer = CustomerOrdersSerializer(order, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #gets the last order created MUST change for production as there could be errors with user orders
            customer_order = CustomerOrders.objects.last()
            print(date(customer_order.order_date.year, 12, 30))
            #Creates an order status based on the most recent order created
            if date((customer_order.order_date.year - 1), 12, 20) <= customer_order.order_date and customer_order.order_date <= date(customer_order.order_date.year, 3, 18):
                new_season = OrderSeason.objects.create(order_id = customer_order)
                new_season.season = new_season.Season.WINTER
                new_season.save()
            elif date(customer_order.order_date.year, 3, 19) <= customer_order.order_date and customer_order.order_date <= date(customer_order.order_date.year, 6, 19):
                new_season = OrderSeason.objects.create(order_id = customer_order)
                new_season.season = new_season.Season.SPRING
                new_season.save()
            elif date(customer_order.order_date.year, 6, 20) <= customer_order.order_date and customer_order.order_date <= date(customer_order.order_date.year, 9, 21):
                new_season = OrderSeason.objects.create(order_id = customer_order)
                new_season.season = new_season.Season.SUMMER
                new_season.save()
            elif date(customer_order.order_date.year, 9, 22) <= customer_order.order_date and customer_order.order_date <= date(customer_order.order_date.year, 12, 19):
                new_season = OrderSeason.objects.create(order_id = customer_order)
                new_season.season = new_season.Season.SUMMER
                new_season.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderSeasonViewSet(ListCreateAPIView):
    queryset = OrderSeason.objects.all()
    serializer_class = OrderSeasonSerializer