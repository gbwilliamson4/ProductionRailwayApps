from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils.timezone import datetime
from django.utils import timezone
from django.db.models import Count, FloatField
from django.db.models.functions import Cast
from django.contrib import messages
from django.db import connection
from operator import attrgetter

from datetime import date, timedelta


def index(request):
    """home page"""

    # calculate x days ago
    today = date.today()
    minus_7 = today - timedelta(days=7)
    minus_30 = today - timedelta(days=30)
    period_end_date = Period_End_Dates.objects.latest('period_end_date')
    # print(period_end_date)
    period_end_date = str(period_end_date)

    wins_7 = Player.objects.values('player_name').filter(win__scan_date__gte=minus_7).annotate(
        Count('win__player')).order_by('-win__player__count')

    wins_30 = Player.objects.values('player_name').filter(win__scan_date__gte=minus_30).annotate(
        Count('win__player')).order_by('-win__player__count')

    wins_all = Player.objects.values('player_name').annotate(Count('win__player')).order_by(
        '-win__player__count')

    wins_period = Player.objects.values('player_name').filter(win__scan_date__gte=period_end_date).annotate(
        Count('win__player')).order_by('-win__player__count')

    context = {'wins_7': wins_7, 'wins_30': wins_30, 'wins_period': wins_period, 'wins_all': wins_all}
    return render(request, 'lotteries/index.html', context)


def checkscan(request):
    checkscan = Checkscan.objects.all().order_by('-scan_date')
    winner = Win.objects.order_by('-scan_date').first()
    player_list = calculate_winner()

    for s in checkscan:
        s.totals = s.nonerisa + s.erisa + s.cafeteria + s.operating

    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = CheckscanNumbers()
    else:
        # POST data submitted, process data
        form = CheckscanNumbers(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Numbers submitted successfully')
                save_winner()
                return redirect('lotteries:checkscan')
        except IntegrityError:
            messages.warning(request, 'Info for today has already been submitted.')

    context = {'form': form, 'checkscan': checkscan, 'winner': winner, 'player_list': player_list}
    return render(request, 'lotteries/checkscan.html', context)


def new_player_guess(request):
    # This data will be displayed on a table in new_player_guesses.html
    today = datetime.today()
    player_guesses = Player_Guesses.objects.exclude(scan_date__year=today.year, scan_date__month=today.month,
                                                    scan_date__day=today.day).order_by('-scan_date', 'player')[:30]

    # Display this data above the other table. That way the most current is always on top. Use a separate html table.
    today_player_guesses = Player_Guesses.objects.filter(scan_date__year=today.year, scan_date__month=today.month,
                                                         scan_date__day=today.day).order_by('player')

    # Count how many players are playing today to determine when we reveal all daily guesses.
    participating_players_count = Participating_Players.objects.annotate(
        as_float=Cast('participating_player', FloatField())).get()
    participating_players_count = participating_players_count.as_float

    today_player_guesses_count = len(today_player_guesses)

    # If not everybody has submitted their guess, overwrite today_player_guesses to be empty.
    if today_player_guesses_count < participating_players_count:
        today_player_guesses = ""

    for g in player_guesses:
        g.totals = g.nonerisa + g.erisa + g.cafeteria + g.operating

    for g in today_player_guesses:
        g.totals = g.nonerisa + g.erisa + g.cafeteria + g.operating

    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = PlayerGuessForm()
    else:
        # POST data submitted, process data
        form = PlayerGuessForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Guess successfully submitted!')
                return redirect('lotteries:new_player_guess')
        except IntegrityError:
            messages.warning(request, 'Only one guess allowed per player per day.')

    context = {'form': form, 'player_guesses': player_guesses, 'today_player_guesses': today_player_guesses}
    return render(request, 'lotteries/new_player_guess.html', context)


def calculate_winner():
    # Get winning numbers
    winning_nums = Checkscan.objects.order_by('-scan_date').first()
    cs_date = winning_nums.scan_date

    # Get participating player guesses
    player_guesses = Player_Guesses.objects.filter(scan_date=cs_date)

    player_list = []

    # Next, we get all applicable players from the above query into their own list
    for player in player_guesses:
        off_by_nonerisa = abs(int(player.nonerisa) - int(winning_nums.nonerisa))
        off_by_erisa = abs(int(player.erisa) - int(winning_nums.erisa))
        off_by_caf = abs(int(player.cafeteria) - int(winning_nums.cafeteria))
        off_by_ops = abs(int(player.operating) - int(winning_nums.operating))
        total_off = off_by_nonerisa + off_by_erisa + off_by_caf + off_by_ops

        objPlayer = Player_Compare(player.player)
        objPlayer.off_by_nonerisa = off_by_nonerisa
        objPlayer.off_by_erisa = off_by_erisa
        objPlayer.off_by_caf = off_by_caf
        objPlayer.off_by_ops = off_by_ops
        objPlayer.total_off = total_off
        objPlayer.scan_date = player.scan_date

        player_list.append(objPlayer)

    player_list.sort(key=attrgetter('total_off'))
    return player_list


def save_winner():
    player_list = calculate_winner()
    # Figure out who was the closest in their guesses and save the result in the Win table.
    winner = min(player_list, key=attrgetter('total_off'))
    win = Win(scan_date=winner.scan_date)
    # win.scan_date = winner.scan_date
    win.player = winner.player_name
    print(win.player.id)
    print(win.scan_date)
    win.save()


class Player_Compare:
    def __init__(self, player_name):
        self.player_name = player_name
        self.off_by_nonerisa = 0
        self.off_by_erisa = 0
        self.off_by_caf = 0
        self.off_by_ops = 0
        self.scan_date = 0

        # This will be used in the normal gameplay for finding the winner
        self.total_off = 0
        # PlayerID of 0 will be passed through for the winning numbers


def win_data(request):
    wins = Win.objects.order_by('-scan_date').all()[:30]
    context = {'wins': wins}
    return render(request, 'lotteries/win_data.html', context)


def counting(request):
    # Get the object, get the value, increment by 1, save.
    the_count = Counting.objects.first()

    if the_count is None:
        # Counting.objects.current_count
        new_count = Counting(current_count=1)
        new_count.save()
        the_count = Counting.objects.first()

    # print(the_count.current_count)
    the_count.current_count = the_count.current_count + 1
    the_count.save()
    context = {"the_count": the_count}
    return render(request, 'lotteries/countrefresh.html', context)

def show_count(request):
    the_count = Counting.objects.first()
    context = {"the_count": the_count}
    return render(request, 'lotteries/showcurrentcount.html', context)
