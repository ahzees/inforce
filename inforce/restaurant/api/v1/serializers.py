from rest_framework import serializers
from restaurant.models import Menu, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["name", "votes"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["restaurant", "date", "info"]
