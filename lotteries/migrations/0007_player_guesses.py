# Generated by Django 4.0.4 on 2022-05-20 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0006_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player_Guesses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonerisa', models.IntegerField()),
                ('erisa', models.IntegerField()),
                ('cafeteria', models.IntegerField()),
                ('operating', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotteries.player')),
            ],
        ),
    ]