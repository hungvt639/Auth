from django.db import models
from django.contrib.auth.models import AbstractUser


SEX_CHOICE = [
    (1, "Nam"),
    (2, "Nữ"),
    (0, "Khác")
]


class MyUsers(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    sex = models.IntegerField(choices=SEX_CHOICE, default=1, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    # avatar = models.FileField(blank=True, null=True, default="avt.jpg")