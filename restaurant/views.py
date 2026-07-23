from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Dish
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Category
from django.shortcuts import redirect, get_object_or_404
from .models import Dish, CartItem
from django.db.models import Sum
from .models import CartItem

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

def menu_view(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})

def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, dish=dish)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')


def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.dish.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)