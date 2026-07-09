from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Dish
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('menu')
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def menu_view(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})
