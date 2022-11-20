from django.contrib import admin

# Register your models here.
# from lotteries.models import Topic, Entry, Plan, Contact, Plan_Contact, Checkscan
from lotteries.models import *

admin.site.register(Checkscan)
admin.site.register(Participating_Players)
admin.site.register(Period_End_Dates)

admin.site.register(Player)
admin.site.register(Player_Guesses)
admin.site.register(Win)
