from django.shortcuts import render
from.models import Category

def Category_view(request):

    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, "products/design.html", context)


