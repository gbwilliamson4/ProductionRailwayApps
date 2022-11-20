# Generated by Django 4.1.1 on 2022-11-12 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0017_incomemaster_needed_inventory_purchased_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomedetail',
            name='type',
            field=models.CharField(default='card', max_length=30),
        ),
        migrations.AlterField(
            model_name='stocking_history',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 12, 14, 42, 39, 947394, tzinfo=datetime.timezone.utc)),
        ),
    ]