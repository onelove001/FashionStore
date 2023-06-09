# Generated by Django 3.1.4 on 2022-08-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('message_sub', models.CharField(blank=True, max_length=40, null=True)),
                ('message_text', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
