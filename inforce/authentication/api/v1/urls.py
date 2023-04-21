from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("v1/auth/register", views.CreateCustomUserApiView.as_view(), name="register"),
    path("v1/auth/login", TokenObtainPairView.as_view(), name="jwt-login"),
    path("v1/auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
]
