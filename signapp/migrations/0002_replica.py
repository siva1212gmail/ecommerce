# Generated by Django 5.0.7 on 2024-08-27 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstdetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='signapp.first')),
            ],
        ),
    ]
