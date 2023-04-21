import datetime

from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.models import Menu, Restaurant, Vote

from . import serializers as sz

# Create your views here.


class RestrauntApiView(generics.CreateAPIView):
    serializer_class = sz.RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]


class MenuApiView(generics.CreateAPIView):
    serializer_class = sz.MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "created"}, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "error - Invalid data"}, status=status.HTTP_406_NOT_ACCEPTABLE
        )


class CurrentDayMenuApiView(views.APIView):
    serializer_class = sz.MenuSerializer

    def get(self, request, pk):
        instance = get_object_or_404(Restaurant, pk=pk)
        if instance := instance.get_current_menu():
            return Response(
                self.serializer_class(instance=instance).data, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No avaliable menu"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class VoteForMenuApiView(generics.CreateAPIView):
    serializer_class = sz.VoteSerializer
    queryset = Vote.objects.all()
