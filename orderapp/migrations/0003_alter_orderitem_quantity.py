# Generated by Django 3.2.8 on 2022-02-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_alter_orderitem_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity'),
        ),
    ]
