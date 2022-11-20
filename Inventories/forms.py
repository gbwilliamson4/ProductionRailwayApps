from django import forms
from .models import *
from django.forms import ModelForm
from django import forms


# class Item_Form(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'total_price', 'quantity']
#         labels = {'name': 'Item Name', 'total_price': 'Total Price', 'quantity': 'Quantity'}


class Item_Form(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'quantity', 'total_price')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01})
        }

        labels = {'name': 'Item Name', 'quantity': 'Quantity', 'total_price': 'Total Price', }

# How to re order things in modelform:
# https://stackoverflow.com/questions/2997168/how-do-i-specify-an-order-of-values-in-drop-down-list-in-a-django-modelform
class Needed_Inventory_Form(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Needed_Inventory_Form, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = self.fields['item'].queryset.order_by('name')

    class Meta:
        model = Needed_Inventory
        ordering = ['item']
        fields = ('item',)

        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {'item': 'Item Name'}


# # This one is the original. It works fine, its just not in order.
# class Needed_Inventory_Form(ModelForm):
#     class Meta:
#         model = Needed_Inventory
#         fields = ('item',)
#
#         widgets = {
#             # 'item': forms.ComboField(),
#             'item': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#         labels = {'item': 'Item Name'}
