# Generated by Django 5.0.7 on 2024-08-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0002_replica'),
    ]

    operations = [
        migrations.AddField(
            model_name='replica',
            name='age',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
