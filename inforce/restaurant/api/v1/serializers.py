from rest_framework import serializers
from restaurant.models import Menu, Restaurant, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "pk",
            "name",
        ]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["pk", "restaurant", "date", "info"]


class VoteSerializer(serializers.ModelSerializer):
    count_of_votes = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        fields = ["pk", "menu", "count_of_votes"]

    def get_count_of_votes(self, obj):
        return obj.get_count_of_votes()
