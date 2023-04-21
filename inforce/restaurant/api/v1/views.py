from django.shortcuts import render
from rest_framework import generics
from restaurant.models import Menu, Restaurant

from . import serializers as sz


# Create your views here.
class RestrauntApiView(generics.CreateAPIView):
    serializer_class = sz.RestaurantSerializer
    queryset = Restaurant.objects.all()
