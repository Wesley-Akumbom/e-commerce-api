# Generated by Django 4.2.6 on 2024-05-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='store',
            new_name='stores',
        ),
    ]
