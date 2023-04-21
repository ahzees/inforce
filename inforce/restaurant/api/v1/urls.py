from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/restaurants/", views.RestrauntApiView.as_view(), name="restaurants"
    ),  # create restaurants
    path(
        "v1/restaurants/<int:pk>/menu/current/",
        views.CurrentDayMenuApiView.as_view(),
        name="current_menu",
    ),  # show today`s menu`
    path(
        "v1/menu/", views.MenuApiView.as_view(), name="upload_menu"
    ),  # uploading a menu
    path(
        "v1/menu/vote/", views.VoteForMenuApiView.as_view(), name="vote_for_menu"
    ),  # vote for menu
    path(
        "v1/vote/current/", views.VoteForMenuApiView.as_view(), name="current_vote"
    ),  # getting result of current day`s voting
]
