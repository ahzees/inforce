import datetime

from django.contrib.auth import get_user_model
from restaurant.models import Menu, Vote

User = get_user_model()


def vote_for_menu(menu_id: int, user_id: int):

    try:
        menu = Menu.objects.get(pk=menu_id)
        user = User.objects.get(pk=user_id)
    except (Menu.DoesNotExist, User.DoesNotExist):
        return None

    vote, created = Vote.objects.get_or_create(menu=menu)
    if user not in vote.count_of_votes.all():
        vote.count_of_votes.add(user)
        return True
    return False


def get_current_menu(restaurant_pk):
    date_now = datetime.datetime.now().date()
    if x := Menu.objects.filter(restaurant__pk=restaurant_pk, date=date_now).first():
        return x
    return None
