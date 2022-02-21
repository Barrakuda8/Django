# Generated by Django 3.2.8 on 2022-02-16 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lootapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skinshard',
            old_name='champ',
            new_name='skin',
        ),
        migrations.AddField(
            model_name='champshard',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='champshard',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authapp.player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skinshard',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='skinshard',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authapp.player'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PurchasedMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootapp.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
