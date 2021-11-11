from django.shortcuts import render
from mainapp.models import CollectionCategory, Champion

# Create your views here.


def loot(request, name=None):
    context = {
        'title': 'Loot',
        'categories': CollectionCategory.objects.all(),
        'champions': Champion.objects.all()
    }
    return render(request, 'lootapp/loot.html', context=context)