from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('design/', views.design_view, name='design'),
    path('test/', views.test_view, name='test'),
    path('portfolio/', views.Portfolio_view, name='portfolio'),
    path('about/About-us/', views.About_view, name="aboutus"),
    path('about/Frequently-asked-questions/', views.Faqs_view, name="faqs")
    ]