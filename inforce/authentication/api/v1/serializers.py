from authentication.models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
