# Generated by Django 3.1 on 2020-08-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
