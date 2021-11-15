from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import CollectionCategory, Champion

# Create your views here.


@login_required
def loot(request, name=None):
    context = {
        'title': 'Loot',
        'player': request.user,
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all()
    }
    return render(request, 'lootapp/loot.html', context=context)