from django.urls import path, include
from . import views

urlpatterns = [
    path('portfolio/', views.Portfolio_view, name='portfolio'),
    ]