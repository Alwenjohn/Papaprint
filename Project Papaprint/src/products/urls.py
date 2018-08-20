from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('design/', views.design_view, name='design'),
    path('test/', views.test_view, name='test')

    ]