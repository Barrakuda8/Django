# Generated by Django 3.2.8 on 2022-02-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lootapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='quantity',
            field=models.SmallIntegerField(default=1000, verbose_name='quantity'),
        ),
    ]
