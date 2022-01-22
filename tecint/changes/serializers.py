#Serialization is the process of converting a Model to JSON.

#import libraries here
from rest_framework import serializers
from .models import DateWeather, BecameBad

#class method to specify what we wish to serialize the
class DateWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateWeather
        fields = ['date', 'was_rainy']
        
class BecameBadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecameBad
        fields = ('date', 'became_bad')
    