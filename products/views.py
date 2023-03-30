from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact Us'})

def products(request):
    return render(request, 'products/product001.html', {'title': 'Products'})