from django import forms
# from .models import Topic, Checkscan
from .models import *


# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         lables = {'text': ''}


class CheckscanNumbers(forms.ModelForm):
    class Meta:
        model = Checkscan
        fields = ['nonerisa', 'erisa', 'cafeteria', 'operating']
        labels = {'nonerisa': 'Non-Erisa', 'erisa': 'Erisa', 'cafeteria': 'Cafeteria', 'operating': 'Operating'}
        # fields = ['nonerisa']
        # labels = {'nonerisa': ''}


class PlayerGuessForm(forms.ModelForm):
    # def __init__(self):
    #     super(PlayerGuessForm, self).__init__(self)
    #     self.fields['player'].queryset = Player.objects.filter(active=True)

    class Meta:
        model = Player_Guesses
        fields = ['player', 'nonerisa', 'erisa', 'cafeteria', 'operating']
        labels = {'player': 'Player', 'nonerisa': 'Non-Erisa', 'erisa': 'Erisa', 'cafeteria': 'Cafeteria', 'operating': 'Operating'}
