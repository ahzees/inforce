from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/restaurants/", views.CreateRestaurantApiView.as_view(), name="restaurants"
    ),  # create restaurants
    path(
        "v1/restaurants/<int:pk>/menu/current/",
        views.GetCurrentDayMenuApiView.as_view(),
        name="current_menu",
    ),  # show today`s menu`
    path(
        "v1/menu/", views.CreateMenuApiView.as_view(), name="upload_menu"
    ),  # uploading a menu
    path(
        "v1/menu/vote/", views.CreateVoteForMenuApiView.as_view(), name="vote_for_menu"
    ),  # vote for menu
    path(
        "v1/vote/current/",
        views.GetCurrentVoteForMenuApiView.as_view(),
        name="all_current_vote",
    ),  # getting result of current day`s voting
]
