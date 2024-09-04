from django.urls import path
from main.views import show_home

app_name = 'home'
urlpatterns = [
    path('', show_home, name='show_home')
]
