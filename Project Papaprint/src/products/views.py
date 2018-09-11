from django.shortcuts import render
from .models import Carousel, Report, Category, Item
from io import BytesIO
from PIL import Image
import re, base64


def homepage_view(request):
    carousel = Carousel.objects.all()

    context = {
        'carousel': carousel
    }
    return render(request, "home.html", context)

def design_view(request):
    report = Report.objects.all()

    context = {
        'report': report
    }
    return render(request, "products/design.html", context)

def test_view(request):
    return render(request, "products/test.html")

def Portfolio_view(request):
    category = Category.objects.all()
    item = Item.objects.all()


    context = {
        'category': category,
        'item': item
    }
    return render(request, "products/portfolio.html", context)

def About_view(request):
    return render(request, "products/about.html")

def Faqs_view(request):
    return render(request, "products/faqs.html")

def Contact_view(request):
    return render(request, "products/contact.html")
