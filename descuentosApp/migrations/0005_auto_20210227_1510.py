# Generated by Django 3.1.3 on 2021-02-27 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descuentosApp', '0004_auto_20210227_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='iso2',
        ),
        migrations.RemoveField(
            model_name='country',
            name='iso3',
        ),
    ]
