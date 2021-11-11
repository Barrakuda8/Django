from django.db import models
from django.conf import settings
from mainapp.models import Champion, Skin


class ChampionBasket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='champ_basket')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)


class SkinBasket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skin_basket')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)
