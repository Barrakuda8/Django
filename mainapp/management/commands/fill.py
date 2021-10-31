import json
from django.conf import settings
from django.core.management.base import BaseCommand
from authapp.models import Player
from mainapp.models import Champion, CollectionCategory, Icon


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        champions = load_from_json('champions')
        icons = load_from_json('icons')

        CollectionCategory.objects.all().delete()
        for category in categories:
            CollectionCategory.objects.create(**category)

        Champion.objects.all().delete()
        for champion in champions:
            category_name = champion['category']
            category_item = CollectionCategory.objects.get(name=category_name)
            champion['category'] = category_item
            Champion.objects.create(**champion)

        Icon.objects.all().delete()
        for icon in icons:
            Icon.objects.create(**icon)

        Player.objects.create_superuser(username='django', password='geekbrains', nickname='Django', age=18)