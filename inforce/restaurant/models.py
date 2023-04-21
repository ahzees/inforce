from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    votes = models.IntegerField(default=0)


class Menu(models.Model):
    restaurant = models.ManyToManyField(Restaurant, related_name="menu")
    date = models.DateTimeField()
    info = models.TextField()
