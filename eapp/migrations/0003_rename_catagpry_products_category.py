# Generated by Django 5.0.6 on 2024-07-11 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_products_alter_contact_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagpry',
            new_name='category',
        ),
    ]