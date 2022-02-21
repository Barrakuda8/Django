# Generated by Django 3.2.8 on 2022-02-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, upload_to='loot')),
                ('price_rp', models.PositiveBigIntegerField(blank=True, verbose_name='price rp')),
                ('is_purchasable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SkinShard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.skin')),
            ],
        ),
        migrations.CreateModel(
            name='ChampShard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.champion')),
            ],
        ),
    ]