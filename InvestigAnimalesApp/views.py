from django.shortcuts import render
from .models import Animal
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, "index.html")

def animales(request):

    listadoAnimales = Animal.objects.all()

    return render(request, "animales.html", {"listaAnimales":listadoAnimales})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            user = authenticate(username = username, password = password, email = email, first_name = first_name)
            login(request, user)
            redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "signup.html",{"form":form})