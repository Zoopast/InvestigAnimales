from django.urls import path
from InvestigAnimalesApp import views

urlpatterns = [
    path('index/', views.home, name="index"),
]
