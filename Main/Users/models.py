from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUsers(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    sex = models.IntegerField(default=1, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)