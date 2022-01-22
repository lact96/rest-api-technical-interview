# import libraries here 
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BecameBadViewSet
from . import views



urlpatterns = [
    path("weather_list/", views.weather_list),
    path("weather/became_bad/", BecameBadViewSet.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)