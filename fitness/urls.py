from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('bmi/', views.bmi, name='bmi'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('exercise/', views.exercise, name='exercise'),

]
