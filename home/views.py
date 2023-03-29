from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact Us'})