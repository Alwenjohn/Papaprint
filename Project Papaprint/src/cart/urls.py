from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_home, name="cart")
    ]