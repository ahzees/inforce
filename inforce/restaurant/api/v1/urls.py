from django.urls import path

from . import views

urlpatterns = [path("v1/restaurant/", views.RestrauntApiView.as_view())]
