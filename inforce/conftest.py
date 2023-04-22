import datetime
import os

import django
import pytest
import pytz
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inforce.settings")
django.setup()

from authentication.models import CustomUser
from django.urls import reverse
from rest_framework.test import APIClient

tz = pytz.timezone("Europe/Kiev")
dt = datetime.datetime.now(tz)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def custom_user():
    data = {
        "email": "test@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "testpassword",
    }
    CustomUser.objects.create_user(**data)
    return CustomUser.objects.first()


@pytest.fixture
def jwt_auth(api_client, custom_user):
    url = reverse("jwt-login")
    data = {"email": custom_user.email, "password": "testpassword"}

    response = api_client.post(url, data)
    return {"HTTP_AUTHORIZATION": f"Bearer {response.data['access']}"}


@pytest.fixture
def restaurant(api_client, jwt_auth):
    url = reverse("restaurants")
    data = {"name": "Chelentano"}

    response = api_client.post(url, data=data, **jwt_auth)

    return response.data["pk"]


@pytest.fixture
def test_creating_menu(api_client, jwt_auth, restaurant):

    url = reverse("upload_menu")
    data = {
        "restaurant": restaurant,
        "date": str(dt.date()),
        "info": "Obid - Borsch, Vecherya - Varenyky ",
    }

    response = api_client.post(url, data=data, **jwt_auth)
    return response.data["menu_id"]
