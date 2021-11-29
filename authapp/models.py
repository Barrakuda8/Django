from datetime import datetime, timedelta
import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Player(AbstractUser):
    nickname = models.CharField(max_length=16, unique=True, verbose_name='nickname')
    icon = models.ImageField(default='icons/Gromp.png', verbose_name='icon')
    age = models.PositiveSmallIntegerField(verbose_name='age')
    blue_essence = models.PositiveSmallIntegerField(verbose_name='blue essence balance', default=0)
    rp = models.PositiveSmallIntegerField(verbose_name='rp balance', default=0)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    email = models.EmailField(verbose_name='email')
    activation_key = models.CharField(max_length=128, blank=True, null=True)
    activation_key_expires = models.DateTimeField(blank=True, null=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activation_key_expires + timedelta(hours=48):
            return True
        return False

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
