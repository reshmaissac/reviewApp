import requests
from django.shortcuts import render, redirect
from .serializers import ProductSerializer
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
from django.db.models import Q 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from django.contrib import messages
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
# function to list products and search products in home page
def home(request):
	query = request.GET.get("q")
	allproducts = None
	if query:
		allproducts = Product.objects.filter(
			Q(name__icontains=query) | Q(brand__icontains=query) | Q(category__name__icontains=query))
		#(name__icontains=query).filter(brand__icontains=query).filter(category__icontains=query)
	else:	
		allproducts = Product.objects.all().order_by('id')
	
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
			messages.warning(request, 'Only admin can perform this task. Please login as admin.')
			return redirect("products:home")
	return redirect("users:login")

def allreviews(request, id):

	result=loadReviews(request, id)
	return HttpResponse(result)

def detail(request,id):

	if request.user.is_authenticated:
		
		if request.method == "POST":
			product=Product.objects.get(id=id)
			rating= request.POST.get('rating','')
			comment=request.POST.get('comment','')
			current_user= request.user
			user_id=current_user.id
			if comment:
				review=Review.objects.create(
					product=product,
					rating=rating,
					comment=comment,
					user=request.user,
    				date_time=date.today(),

				)
			return redirect('/details/{}/'.format(id))	

		else:
			
			product = Product.objects.get(id=id)
			result=loadProduct(request, id)
			return HttpResponse(result)
	else:
		return redirect("users:login")

def edit(request, id):
    review = Review.objects.get(id=id)
    if request.method == "POST":
        product = review.product
        product_id = product.id
        review.id = id
        # form = EmployeeForm(request.POST, instance = review)
        review.rating = request.POST.get("rating", '')
        review.comment = request.POST.get("comment", '')
        review.date_time = date.today()
        review.user = request.user
        if review.comment:
            review.save()
            return redirect(reverse('products:detail', kwargs={'id': product_id}))
    else:
        return render(request, "products/editReview.html", {"review": review})


def destroy(request, id):  
	review = Review.objects.get(id=id)
	product = review.product
	product_id = product.id
	review.delete()
	return redirect(reverse('products:detail', kwargs={'id': product_id}))
	

def loadProduct(request,id):

	if request.user.is_authenticated:
		product=Product.objects.get(id=id)
		reviews = Review.objects.filter(product=id).order_by("-comment")
		average = reviews.aggregate(Avg("rating"))["rating__avg"]
		if average == None:
			average=0
		else:
			average = round(average,2)
		
		
		context={
			"prod":product,
			"reviews":reviews,
			"average":average,
		}
					
		return render(request,'products/product001.html',context)
	
def loadReviews(request,id):

	if request.user.is_authenticated:
		product=Product.objects.get(id=id)
		
		context={
			"prod":product,
		}
					
		return render(request,'products/allReviews.html',context)	
	
def viewReview(request,id):

	if request.user.is_authenticated:
		review=Review.objects.get(id=id)
		product = review.product
		product_id = product.id
		
		
        
		return render(request, "products/productReview.html", {"review": review, "product": product})
		
	else:
		return redirect("users:login")	

@api_view(['GET'])
def getProducts(request):
	products = Product.objects.all().order_by('id')
	serializer = ProductSerializer(products, many= True)
	return Response(serializer.data)



class ProductList(APIView):
	serializer_class = ProductSerializer
	def post(self, request):
		if request.user.is_authenticated:
			serializer = ProductSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
			else:
				return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
		 
		 
	def get(self, request, id=None):
		if id:
			products = Product.objects.all().order_by('id')
			serializer = ProductSerializer(products)
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
		items = Product.objects.all()
		serializer = ProductSerializer(items, many=True)
		return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

