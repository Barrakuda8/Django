from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from mainapp.models import CollectionCategory, Champion, Skin
from basketapp.models import ChampionBasket, SkinBasket
import random

# Create your views here.


@login_required
def collection(request, name=None):

    basket_champ = ChampionBasket.objects.filter(user=request.user).first()
    basket_skin = SkinBasket.objects.filter(user=request.user).first()

    if basket_champ:
        owned_champs = basket_champ.get_owned()

        if basket_skin:
            owned_skins = basket_skin.get_owned()
        else:
            owned_skins = []
    else:
        owned_champs = []
        owned_skins = []

    context = {
        'title': 'Collection',
        'player': request.user,
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all(),
        'skins': Skin.objects.all(),
        'owned_champs': owned_champs,
        'owned_skins': owned_skins,
        'epic_skins': SkinBasket.get_division(owned_skins, 'epic'),
        'legendary_skins': SkinBasket.get_division(owned_skins, 'legendary'),
        'mythic_skins': SkinBasket.get_division(owned_skins, 'mythic'),
        'absolute_skins': SkinBasket.get_division(owned_skins, 'absolute')
    }
    if name is None:
        page = f'collectapp/champions.html'
    else:
        get_object_or_404(CollectionCategory, name=name)
        page = f'collectapp/{name}.html'
        context['title'] = name.title()
    return render(request, page, context=context)


@login_required
def product(request, cat=None, pk=None):

    skins = []

    if cat == "champions":
        product = get_object_or_404(Champion, pk=pk)
        skins = Skin.objects.filter(champion__pk=pk)
    elif cat == "skins":
        product = get_object_or_404(Skin, pk=pk)
        skins = random.sample(list(Skin.objects.all().exclude(pk=pk)), 5)

    context = {
        'title': product.name,
        'player': request.user,
        'categories': CollectionCategory.objects.all(),
        'product': product,
        'skins': skins,
        'owned_skins': SkinBasket.objects.filter(user=request.user).values_list('skin', flat=True),
        'owned_champs': ChampionBasket.objects.filter(user=request.user).values_list('champion', flat=True)
    }

    page = f'collectapp/{cat[:-1]}.html'

    return render(request, page, context=context)
