from django.urls import path
from InvestigAnimalesApp import views


urlpatterns = [
    path('index/', views.home, name="index"),
    path('animales/', views.animales, name="animales"),
    path('signup/', views.signup, name="signup")
]