# Generated by Django 2.2.4 on 2022-06-25 20:50

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('wishlist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Wishlist',
        ),
    ]
