# Generated by Django 4.0.4 on 2022-05-20 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0011_rename_wins_win'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Win',
        ),
    ]
