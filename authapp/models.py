from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    nickname = models.CharField(max_length=16, unique=True, verbose_name='nickname')
    icon = models.ImageField(default='icons/Gromp.png', verbose_name='icon')
    age = models.PositiveSmallIntegerField(verbose_name='age')

