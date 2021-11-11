from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import ChampionBasket, SkinBasket
from mainapp.models import Champion, Skin


def basket(request):
    pass


def add(request, cat=None, pk=None):

    if cat == 'champions':
        champ = get_object_or_404(Champion, pk=pk)

        if not ChampionBasket.objects.filter(champion=champ, user=request.user):
            basket_item = ChampionBasket(champion=champ, user=request.user)
            basket_item.save()

    elif cat == 'skins':
        skin = get_object_or_404(Skin, pk=pk)

        if not SkinBasket.objects.filter(skin=skin, user=request.user) \
                and ChampionBasket.objects.filter(champion=skin.champion, user=request.user):
            basket_item = SkinBasket(skin=skin, user=request.user, champion=skin.champion)
            basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, cat=None, pk=None):

    if cat == 'champions':
        champ = get_object_or_404(Champion, pk=pk)

        if ChampionBasket.objects.filter(champion=champ, user=request.user) \
                and not SkinBasket.objects.filter(champion=champ, user=request.user):
            ChampionBasket.objects.get(champion=champ, user=request.user).delete()

    if cat == 'skins':
        skin = get_object_or_404(Skin, pk=pk)

        if SkinBasket.objects.filter(skin=skin, user=request.user):
            SkinBasket.objects.get(skin=skin, user=request.user).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



