import datetime

from django.shortcuts import get_object_or_404, render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.models import Menu, Restaurant, Vote

from . import serializers as sz

# Create your views here.


class CreateRestaurantApiView(generics.CreateAPIView):
    """Add Restaurant"""

    serializer_class = sz.RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]


class CreateMenuApiView(generics.CreateAPIView):
    """Upload Menu"""

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


class GetCurrentDayMenuApiView(views.APIView):
    """Get a current menu"""

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


@extend_schema(request=sz.VotebyUserSerializer)
class CreateVoteForMenuApiView(views.APIView):
    """Vote for menu"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data)
        if request.user.vote(request.data["menu"], Vote):
            return Response(
                {"status": "You have voted succesfuly"}, status=status.HTTP_200_OK
            )
        return Response(
            {"status": "error - vote does`nt exist"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
