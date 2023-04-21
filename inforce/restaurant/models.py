import datetime

from authentication.models import CustomUser
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    """Restaurant model"""

    name = models.CharField(max_length=255, unique=True)

    def get_current_menu(self):
        date_now = datetime.datetime.now().date()
        if x := Menu.objects.filter(restaurant__pk=self.pk, date=date_now).first():
            return x


class Menu(models.Model):
    """Menu model"""

    restaurant = models.ForeignKey(
        Restaurant,
        related_name="menu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.DateField()
    info = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["restaurant", "date"], name="unique_menu")
        ]


class Vote(models.Model):
    """Vote model"""

    menu = models.ForeignKey(Menu, related_name="vote", on_delete=models.PROTECT)
    count_of_votes = models.ManyToManyField(CustomUser, related_name="votes")
    created_at = models.DateField(auto_now=True)

    def get_count_of_votes(self):
        return self.count_of_votes.all().count()
