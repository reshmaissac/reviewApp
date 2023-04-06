from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.
def home(request):
	query = request.GET.get("q")
	allproducts = None
	if query:
		allproducts = Product.objects.filter(name__icontains=query)
	else:	
		allproducts = Product.objects.all()
		print("Hello {0} ..".format(allproducts))
	context = {
    	"product":allproducts,
    }
	return render(request,'home/home.html',context)

def detail(request,id):
	product=Product.objects.get(id=id)
	""" reviews = Review.objects.filter(product=id).order_by("-comment")

	average = reviews.aggregate(Avg("rating"))["rating__avg"]
	if average == None:
		average=0
	else:
		average = round(average,2) """
	reviews = "sample review"
	average = 9
	context={
		"prod":product,
		"reviews":reviews,
		"average":average,
	}
	return render(request,'products/details.html',context)

def add_products(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			if request.method == "POST":
				form = ProductForm(request.POST or None, request.FILES)

				if form.is_valid():
					data = form.save(commit=False)
					data.save()
					return redirect("products:home")
			else:
				form = ProductForm()
			return render(request,'products/add_products.html',{"form":form,"controller":"Add Products"})
		else:
			return redirect("products:home")
	return redirect("users:login")







# Create your views here.
def home(request):
    return render(request, 'home/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact Us'})

def products(request):
    return render(request, 'products/product001.html', {'title': 'Products'})
