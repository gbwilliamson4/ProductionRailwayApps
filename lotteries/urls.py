"""Defines URL patterns for lotteries"""

# from django.template.defaulttags import url
# from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'lotteries'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path(r'checkscan/', views.checkscan, name='checkscan'),
    path('checkscan/', views.checkscan, name='checkscan'),
    path('new_player_guess/', views.new_player_guess, name='new_player_guess'),
    path('win_data/', views.win_data, name='win_data'),
    path('counting/', views.counting, name='counting')
]
