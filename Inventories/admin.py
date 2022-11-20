from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Item)
admin.site.register(Needed_Inventory)
admin.site.register(Purchase_History)
admin.site.register(Vending_Location)
admin.site.register(Stocking_History)
admin.site.register(IncomeMaster)
admin.site.register(IncomeDetail)
