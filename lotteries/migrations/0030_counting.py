# Generated by Django 4.1.3 on 2023-07-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0029_remove_player_guesses_unique_player_date_guess_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_count', models.IntegerField()),
            ],
        ),
    ]