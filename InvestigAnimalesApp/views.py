from django.shortcuts import render
from .models import Animal
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def animales(request):

    listadoAnimales = Animal.objects.all()

    return render(request, "animales.html", {"listaAnimales":listadoAnimales})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            print("hola mundo")
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, "signup.html",{'form':form})