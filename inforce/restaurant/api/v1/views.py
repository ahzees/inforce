import datetime

import pytz
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404, render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.models import Menu, Restaurant, Vote

from . import serializers as sz
from .services import get_current_menu, vote_for_menu

# Create your views here.


@extend_schema(
    description="This URL is used to create a new restaurant.\
        It requires an authenticated user and expects a POST\
        request with a serialized restaurant object."
)
class CreateRestaurantApiView(generics.CreateAPIView):
    """Add Restaurant"""

    serializer_class = sz.RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema(
    description="This URL is used to upload a new menu. \
        It requires an authenticated user and expects a POST\
        request with a serialized menu object."
)
class CreateMenuApiView(generics.CreateAPIView):
    """Upload Menu"""

    serializer_class = sz.MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {"status": "created", "menu_id": serializer.data["pk"]},
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError:
                return Response(
                    {"status": "error - menu have already"},
                    status=status.HTTP_409_CONFLICT,
                )
        return Response(
            {"status": "error - Invalid data"},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )


@extend_schema(
    description="This URL is used to retrieve the menu of a specific\
        restaurant for the current day. It expects a GET request\
        with the primary key (pk) of the restaurant in the URL path."
)
class GetCurrentDayMenuApiView(views.APIView):
    """Get a current menu"""

    serializer_class = sz.MenuSerializer

    def get(self, request, pk):
        instance = get_object_or_404(Restaurant, pk=pk)
        if instance := get_current_menu(instance.pk):
            return Response(
                self.serializer_class(instance=instance).data, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No avaliable menu"}, status=status.HTTP_404_NOT_FOUND
        )


@extend_schema(
    request=sz.VotebyUserSerializer,
    description=" This URL is used to vote for a menu. It requires\
                an authenticated user and expects a POST request with \
                aserialized object containing the ID of the menu being voted for.",
)
class CreateVoteForMenuApiView(views.APIView):
    """Vote for menu"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        access = vote_for_menu(request.data["menu"], request.user.pk)
        if access:
            return Response(
                {"status": "You have voted succesfuly"}, status=status.HTTP_200_OK
            )
        return Response(
            {"status": "error"},
            status=status.HTTP_404_NOT_FOUND,
        )


@extend_schema(
    description="This URL is used to retrieve the current day's \
                voting results. It expects a GET request and returns a \
                list of all the votes cast for the menus available on that day."
)
class GetCurrentVoteForMenuApiView(generics.ListAPIView):
    """Get a list of all votes for the current day"""

    serializer_class = sz.VoteSerializer
    queryset = Vote.objects.all()

    def get_queryset(self):
        tz = pytz.timezone("Europe/Kiev")
        dt = datetime.datetime.now(tz)
        date_now = dt.date()
        items = Vote.objects.filter(menu__date=date_now).all()
        return items
