from django.urls import path
from .views import daily_habits

urlpatterns = [
    path('', daily_habits, name='daily_habits'),
]
