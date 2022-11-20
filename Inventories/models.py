from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=35)
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()
    image_url = models.URLField(null=True, default=None)

    def __str__(self):
        return self.name


class Vending_Location(models.Model):
    location_name = models.CharField(max_length=35)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.location_name


class Vending_Inventory(models.Model):
    location = models.ForeignKey(Vending_Location, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.location) + " - " + str(self.item)


class Purchase_History(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Purchase History"

    def __str__(self):
        return str(self.item) + " - " + str(self.purchase_date)


class Needed_Inventory(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)

    # admin_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Needed Inventory"

    def __str__(self):
        return str(self.item)


class Stocking_History(models.Model):
    location = models.ForeignKey(Vending_Location, on_delete=models.CASCADE)
    stock_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.location) + " - " + str(self.stock_date)


class IncomeMaster(models.Model):
    daterange = models.CharField(max_length=100)

    def __str__(self):
        return self.daterange


class IncomeDetail(models.Model):
    daterange = models.ForeignKey(IncomeMaster, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    transactions = models.IntegerField()
    net_amnt = models.DecimalField(decimal_places=2, max_digits=6)
    type = models.CharField(max_length=30, choices=(('cash', 'cash'), ('card', 'card')))

    def __str__(self):
        return self.location
