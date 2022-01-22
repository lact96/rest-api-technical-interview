from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import serializers
from .serializers import DateWeatherSerializer, BecameBadSerializer
#import Models
from .models import DateWeather, BecameBad
from rest_framework.generics import(
    ListCreateAPIView
)

# Create your views here.
#This function will create a new order and an order status:
@api_view(['GET', 'POST'])
def weather_list(request, format=None):
    #Handles get requests for viewing Order Numbers
    if request.method == 'GET':
        date = DateWeather.objects.all()
        serializer = DateWeatherSerializer(date, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DateWeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #compares the last 2 days entered to see if the weather became "bad"
            date = DateWeather.objects.all().order_by('-date')
            if date[1].was_rainy == False and date[0].was_rainy == True:
                new_date = date[0].date
                print(new_date)
                became_bad = BecameBad.objects.create(date = new_date, became_bad = True)
                #will save the date where it became bad
                became_bad.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Implement Put, Delete methods
              
#Create and add an item to our order_status 
class BecameBadViewSet(ListCreateAPIView):
    queryset = BecameBad.objects.all().order_by('date')
    serializer_class = BecameBadSerializer