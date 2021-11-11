from django.shortcuts import render, get_object_or_404
from mainapp.models import CollectionCategory, Champion, Skin
from basketapp.models import ChampionBasket, SkinBasket

# Create your views here.


def collection(request, name=None):

    owned_champions = ChampionBasket.objects.filter(user=request.user).values_list('champion', flat=True)
    owned_skins = SkinBasket.objects.filter(user=request.user).values_list('skin', flat=True)

    context = {
        'title': 'Collection',
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all(),
        'skins': Skin.objects.all(),
        'owned_champs': owned_champions,
        'owned_skins': owned_skins,
        'epic_skins': owned_skins.filter(skin__division='epic'),
        'legendary_skins': owned_skins.filter(skin__division='legendary'),
        'mythic_skins': owned_skins.filter(skin__division='mythic'),
        'absolute_skins': owned_skins.filter(skin__division='absolute')
    }
    if name is None:
        page = f'collectapp/champions.html'
    else:
        get_object_or_404(CollectionCategory, name=name)
        page = f'collectapp/{name}.html'
        context['title'] = name.title()
    return render(request, page, context=context)
