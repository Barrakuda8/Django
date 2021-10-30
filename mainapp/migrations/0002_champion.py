# Generated by Django 3.2.8 on 2021-10-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, upload_to='champions')),
                ('price_rp', models.PositiveBigIntegerField(verbose_name='price_rp')),
                ('price_be', models.PositiveBigIntegerField(verbose_name='price_blue_essence')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.collectioncategory', verbose_name='category')),
            ],
        ),
    ]
