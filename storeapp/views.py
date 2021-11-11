from django.shortcuts import render, get_object_or_404
from mainapp.models import CollectionCategory, Champion, Skin
from basketapp.models import ChampionBasket, SkinBasket
from django.db.models import Q
from django.http import Http404

# Create your views here.


def store(request, name=None, role=None):

    owned_champions = ChampionBasket.objects.filter(user=request.user).values_list('champion', flat=True)
    owned_skins = SkinBasket.objects.filter(user=request.user).values_list('skin', flat=True)

    # Skin.objects.filter(~Q(pk__in=owned_skins))
    # Champion.objects.filter(~Q(pk__in=owned_champions))

    context = {
        'title': 'Store',
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all(),
        'skins': Skin.objects.all(),
        'owned_champs': owned_champions,
        'owned_skins': owned_skins
    }

    roles = {
        'slayer': ['assassin', 'skirmisher'],
        'fighter': ['juggernaut', 'diver'],
        'mage': ['battlemage', 'burst', 'artillery'],
        'marksman': ['marksman'],
        'tank': ['vanguard', 'warden'],
        'support': ['catcher', 'enchanter']
    }
    
    if role is not None:

        if role not in roles:
            raise Http404

        name = 'champions'

        champions = context['champions'].filter(Q(role__in=roles[role]) | Q(role_b__in=roles[role]))
        context['champions'] = champions

    if name is None:
        page = 'storeapp/store.html'
    else:
        get_object_or_404(CollectionCategory, name=name)
        page = f'storeapp/{name}.html'
        context['title'] = name.title()

    return render(request, page, context=context)
