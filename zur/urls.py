from django.urls import path
from .views import home_view,category_view,listing_view,contact_view

urlpatterns = [
    path('',home_view, name="home-page"),
    path('category/',category_view, name="category-page"),
    path('listing/',listing_view, name="listing-page"),
    path('contact/',contact_view, name="contact-page"),
]
