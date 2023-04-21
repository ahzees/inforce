import json

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_custom_user(api_client):
    # Arrange
    url = reverse("register")
    data = {
        "email": "test@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "testpassword",
    }
    expected_response = {"status": "created"}

    # Act
    response = api_client.post(url, data=data)

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert json.loads(response.content) == expected_response


@pytest.mark.django_db
def test_create_custom_user_invalid_data(api_client):
    # Arrange
    url = reverse("register")
    data = {
        "email": "invalidemail",
        "first_name": "",
        "last_name": "",
        "password": "",
    }

    # Act
    response = api_client.post(url, data=data)

    # Assert
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.django_db
def test_create_custom_user_duplicate_email(api_client, custom_user):
    # Arrange
    url = reverse("register")
    data = {
        "email": custom_user.email,
        "first_name": "John",
        "last_name": "Doe",
        "password": "testpassword",
    }

    # Act
    response = api_client.post(url, data=data)

    # Assert
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.django_db
def test_create_custom_user_missing_field(api_client):
    # Arrange
    url = reverse("register")
    data = {"email": "test@example.com"}

    # Act
    response = api_client.post(url, data=data)

    # Assert
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.django_db
def test_jwt_token(api_client, custom_user):
    # Arrange
    url = reverse("jwt-login")
    data = {"email": custom_user.email, "password": "testpassword"}
    # Act
    response = api_client.post(url, data=data)
    print(response)
    # Assert
    assert response.status_code == status.HTTP_200_OK
