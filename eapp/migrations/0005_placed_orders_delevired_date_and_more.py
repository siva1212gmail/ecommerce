# Generated by Django 5.0.7 on 2024-08-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0004_placed_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed_orders',
            name='delevired_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='placed_orders',
            name='delivery_status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
