# Generated by Django 4.1.1 on 2022-09-21 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
