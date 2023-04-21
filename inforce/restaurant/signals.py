from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Menu, Vote


@receiver(post_save, sender=Menu)
def create_vote_after_creating_menu(sender, instance, created, *args, **kwargs):
    if created:
        print("New menu created, creating vote...")
        Vote.objects.create(menu=instance)
