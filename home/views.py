from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'home/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=['shopgenovia@gmail.com'],
                reply_to=[from_email],
            )

            
            email.send()
            return redirect("home:email-sent")
    return render(request, "home/contactUs.html", {"form": form})

def emailSent(request):
    return render(request, 'home/emailSent.html', {'title': 'Products'})

def products(request):
    return render(request, 'products/product001.html', {'title': 'Products'})