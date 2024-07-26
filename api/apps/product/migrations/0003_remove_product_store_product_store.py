# Generated by Django 4.2.6 on 2024-05-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_store_owner_store_user'),
        ('product', '0002_product_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ManyToManyField(related_name='products', to='store.store'),
        ),
    ]
