# Generated by Django 3.1.3 on 2021-02-27 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descuentosApp', '0011_remove_country_phone_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
    ]
