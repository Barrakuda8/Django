# Generated by Django 3.2.8 on 2022-02-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_order_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'Forming'), ('STP', 'Waiting for payment'), ('PD', 'Paid'), ('DN', 'Done'), ('CN', 'Canceled')], default='FM', max_length=3),
        ),
    ]
