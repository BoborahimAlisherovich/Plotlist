
from django.shortcuts import render


def home_view(request):
    return render(request, "index.html" )

def category_view(request):
    return render(request, "category.html" )

def listing_view(request):
    return render(request, "listing.html" )

def contact_view(request):
    return render(request, "contact.html" )
