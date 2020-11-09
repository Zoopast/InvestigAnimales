from django.urls import path
from InvestigAnimalesApp import views


urlpatterns = [
    path('index/', views.home, name="index"),
    path('animales/', views.animales, name="animales"),
    path('signup/', views.signup, name="signup"),
    path('contactanos/',views.contactanos, name="contactanos"),
    path('objetivo/', views.objetivo, name="objetivo"),
    path('quienessomos/', views.quienessomos, name="quienessomos"),
]