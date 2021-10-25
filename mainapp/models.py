from django.db import models


class CollectionCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=32, unique=True)

    def __str__(self):
        return self.name


class Champion(models.Model):
    category = models.ForeignKey(CollectionCategory, on_delete=models.CASCADE, verbose_name='category')
    name = models.CharField(verbose_name='name', max_length=32, unique=True)
    image = models.ImageField(upload_to='champions', blank=True)
    price_rp = models.PositiveBigIntegerField(verbose_name='price_rp')
    price_be = models.PositiveBigIntegerField(verbose_name='price_blue_essence')

    def __str__(self):
        return self.name


class Skin(models.Model):
    category = models.ForeignKey(CollectionCategory, on_delete=models.CASCADE, verbose_name='category')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, verbose_name='champion')
    name = models.CharField(verbose_name='name', max_length=32, unique=True)
    image = models.ImageField(upload_to='skins', blank=True)
    price_rp = models.PositiveBigIntegerField(verbose_name='price_rp')

    def __str__(self):
        return self.name


