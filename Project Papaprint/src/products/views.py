from django.shortcuts import render
from .models import Carousel


def homepage_view(request):
    carousel = Carousel.objects.all()

    context = {
        'carousel': carousel
    }
    return render(request, "home.html", context)

def design_view(request):
    return render(request, "products/design.html")

