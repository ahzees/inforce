import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_current_day_menu(api_client, jwt_auth, restaurant, test_creating_menu):
    url = reverse("current_menu", kwargs={"pk": restaurant})

    response = api_client.get(url, **jwt_auth)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["pk"] == test_creating_menu


@pytest.mark.django_db
def test_create_vote_for_menu(api_client, jwt_auth, test_creating_menu):
    url = reverse("vote_for_menu")

    data = {"menu": test_creating_menu}

    response = api_client.post(url, data=data, **jwt_auth)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["status"] == "You have voted succesfuly"


@pytest.mark.django_db
def test_get_current_vote_for_menu(api_client, jwt_auth, test_creating_menu):
    url = reverse("all_current_vote")

    response = api_client.get(url, **jwt_auth)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["menu"] == test_creating_menu
