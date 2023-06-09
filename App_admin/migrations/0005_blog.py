# Generated by Django 3.1.4 on 2022-09-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_admin', '0004_auto_20220909_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
