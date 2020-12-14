# Generated by Django 3.1.3 on 2020-11-19 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descuentosApp', '0002_auto_20201119_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descuentosApp.city')),
            ],
        ),
    ]
