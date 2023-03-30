# Generated by Django 3.1.4 on 2022-09-09 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App_admin', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 9, 22, 4, 12, 410250, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='udpated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]