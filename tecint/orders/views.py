from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import serializers
from .serializers import OrderLinesSerializer, OrderNumberSerializer, OrderStatusSerializer
#import Models
from .models import OrderNumber, OrderLines, OrderStatus
from rest_framework.generics import(
    ListCreateAPIView
)

# Create your views here.
#This function will create a new order and an order status:
@api_view(['GET', 'POST'])
def order_list(request, format=None):
    #Handles get requests for viewing Order Numbers
    if request.method == 'GET':
        order = OrderNumber.objects.all()
        serializer = OrderNumberSerializer(order, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #gets the last order created MUST change for production as there could be errors with user orders
            order_number = OrderNumber.objects.last()
            #Creates an order status based on the most recent order created
            new_order_status = OrderStatus.objects.create(order = order_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_num(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = OrderNumber.objects.get(pk=pk)
    except OrderNumber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderNumberSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderNumberSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Will loop through the appropriate order_status and update set an update correctly.

              
#Create and add an item to our order_status 
@api_view(['GET', 'POST'])
def order_items(request, format=None):
    #Handles get requests for viewing Order Numbers
    if request.method == 'GET':
        item = OrderLines.objects.all()
        serializer = OrderLinesSerializer(item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderLinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #gets the last order created MUST change for production as there could be errors with user orders
            order_item = OrderLines.objects.last()
            #Creates an order status based on the most recent order created
            order_status = OrderStatus.objects.get(order=order_item.order_number)
            order_status.items.add(order_item)
            order_status.save()
            #Iterates through order_status M2M items list and checks if they are SHIPPED or PENDING
            for i in order_status.items.all():
                #IF there is atleast one item that is pending will have status as PENDING
                if i.status == 'Pending':
                    order_status.status = order_status.Status.PENDING 
                    order_status.save()
                else:
                    #If all items are shipped or some items are cancelled will save as SHIPPED
                    order_status.status = order_status.Status.SHIPPED
                    order_status.save()
             
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_num(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = OrderLines.objects.get(pk=pk)
    except OrderLines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderLinesSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderLinesSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Creates an order status based on the most recent order created
            order_status = OrderStatus.objects.get(order=order.order_number)
            #Iterates through order_status M2M items list and checks if they are SHIPPED or PENDING
            for i in order_status.items.all():
                #IF there is atleast one item that is pending will have status as PENDING
                if i.status == 'Pending':
                    order_status.status = order_status.Status.PENDING 
                    order_status.save()
                else:
                    #If all items are shipped or some items are cancelled will save as SHIPPED
                    order_status.status = order_status.Status.SHIPPED
                    order_status.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderStatusViewSet(ListCreateAPIView):
    queryset = OrderStatus.objects.all().order_by('order')
    serializer_class = OrderStatusSerializer