from django.db import models
from django.db.models import UniqueConstraint


# python manage.py makemigrations lotteries
# python manage.py migrate
# python manage.py runserver

# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text
#
#
# class Entry(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         return self.text[:50] + "..."




class Checkscan(models.Model):
    scan_date = models.DateField(auto_now_add=True, unique=True)
    nonerisa = models.IntegerField()
    erisa = models.IntegerField()
    cafeteria = models.IntegerField()
    operating = models.IntegerField()

    def __str__(self):
        return str(self.scan_date)


class Player(models.Model):
    player_name = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.player_name


class Player_Guesses(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    scan_date = models.DateField(auto_now_add=True)
    nonerisa = models.IntegerField()
    erisa = models.IntegerField()
    cafeteria = models.IntegerField()
    operating = models.IntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['player', 'scan_date'], name='unique_player_date_guess')
        ]

    def __str__(self):
        return str(self.player) + ": " + str(self.scan_date)


class Win(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    scan_date = models.DateField(auto_now_add=True, unique=True)

    class Meta:
        verbose_name_plural = 'Wins'

    def __str__(self):
        return str(self.player) + ": " + str(self.scan_date)


class Participating_Players(models.Model):
    participating_player = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Participating_Players'

    def __str__(self):
        return str(self.participating_player)


class Period_End_Dates(models.Model):
    period_end_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Period_End_Dates'

    def __str__(self):
        return str(self.period_end_date)


class Counting(models.Model):
    current_count = models.IntegerField()

    def __str__(self):
        return str(self.current_count)
