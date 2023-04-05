from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
from django.db.models import Q 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# function to list products and search products in home page
def home(request):
	query = request.GET.get("q")
	allproducts = None
	if query:
		allproducts = Product.objects.filter(
			Q(name__icontains=query) | Q(brand__icontains=query) | Q(category__icontains=query))
		#(name__icontains=query).filter(brand__icontains=query).filter(category__icontains=query)
	else:	
		allproducts = Product.objects.all()
	
	p = Paginator(allproducts, 3)
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)  # returns the desired page object
	except PageNotAnInteger: 
		# if page_number is not an integer then assign the first page
		page_obj = p.page(1)
	except EmptyPage:
		# if page is empty then return last page
		page_obj = p.page(p.num_pages)
	
	context = {
    	"product":allproducts,
	    'page_obj': page_obj,
    }
	return render(request,'home/home.html',context)

# def detail(request,id):
# 	product=Product.objects.get(id=id)
# 	""" reviews = Review.objects.filter(product=id).order_by("-comment")

# 	average = reviews.aggregate(Avg("rating"))["rating__avg"]
# 	if average == None:
# 		average=0
# 	else:
# 		average = round(average,2) """
# 	reviews = "sample review"
# 	average = 9
# 	context={
# 		"prod":product,
# 		"reviews":reviews,
# 		"average":average,
# 	}
# 	return render(request,'products/details.html',context)
	

#function to upload products by admin
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

def detail(request,id):

	if request.user.is_authenticated:

		if request.method == "POST":
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
			print("test6")

			rating= request.POST.get('rating',3)
			comment=request.POST.get('comment','')
			if comment:
				review=Review.objects.create(
					product=product,
					rating=rating,
					comment=comment,

				)
		else:
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
			
	