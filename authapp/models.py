from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    nickname = models.CharField(max_length=16, unique=True, verbose_name='nickname')
    icon = models.ImageField(default='icons/Gromp.png', verbose_name='icon')
    age = models.PositiveSmallIntegerField(verbose_name='age')
    blue_essence = models.PositiveSmallIntegerField(verbose_name='blue essence balance', default=0)
    rp = models.PositiveSmallIntegerField(verbose_name='rp balance', default=0)

    def add_be(self, amount):
        self.blue_essence += amount
        self.save()

    def add_rp(self, amount):
        self.rp += amount
        self.save()

    def subtract_be(self, amount):
        self.blue_essence -= amount
        self.save()

    def subtract_rp(self, amount):
        self.rp -= amount
        self.save()
