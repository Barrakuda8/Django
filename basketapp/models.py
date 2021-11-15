from django.db import models
from django.conf import settings
from mainapp.models import Champion, Skin


class ChampionBasket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='champ_basket')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    method = models.CharField(max_length=2, verbose_name='payment method')
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)

    def get_owned(self):
        return ChampionBasket.objects.filter(user=self.user).values_list('champion', flat=True)

    @property
    def get_total_cost(self):
        rp = sum(list(map(lambda x: x.champion.price_rp, ChampionBasket.objects.filter(user=self.user, method='rp'))))
        be = sum(list(map(lambda x: x.champion.price_be, ChampionBasket.objects.filter(user=self.user, method='be'))))
        return [rp, be]


class SkinBasket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skin_basket')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)

    def get_owned(self):
        return SkinBasket.objects.filter(user=self.user).values_list('skin', flat=True)

    @staticmethod
    def get_division(skins, div):
        if skins:
            return skins.filter(skin__division=div)
        else:
            return []

    @property
    def get_total_cost(self):
        return sum(list(map(lambda x: x.skin.price_rp, SkinBasket.objects.filter(user=self.user))))