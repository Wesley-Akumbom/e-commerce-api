# Generated by Django 4.2.6 on 2024-05-22 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_user_store_store_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='store_owner',
            new_name='user',
        ),
    ]
