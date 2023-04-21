# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Create custom user model"""

    email = models.EmailField("email address", unique=True, null=False)
    first_name = models.CharField("first_name", max_length=30)
    last_name = models.CharField("last_name", max_length=30)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    last_login = models.DateTimeField("last login", auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def vote(self, menu, Vote):
        if vote := Vote.objects.filter(menu__pk=menu).first():
            vote.count_of_votes.add(self)
            return True
