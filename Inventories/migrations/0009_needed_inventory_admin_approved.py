# Generated by Django 4.1.1 on 2022-09-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0008_needed_inventory_pending_needed_inventory_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='needed_inventory',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
