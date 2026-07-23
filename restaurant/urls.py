from django.contrib import admin
from django.urls import path, include
from restaurant.views import home
from django.urls import path
from . import views
from restaurant.views import home, register, menu_view
urlpatterns = [
    path('', home, name='home'),

    path('register/', register, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('menu/', menu_view, name='menu'),

    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart_view, name='cart'),
]