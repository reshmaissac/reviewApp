import requests
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

@api_view(['GET'])
def get_fakestore_data(request):
    url = 'https://fakestoreapi.com/products/category/electronics'
    response = requests.get(url)
    products = response.json()
    
    return Response(products)

@staff_member_required
def fetch_products(request):
    url = 'https://fakestoreapi.com/products/category/electronics'
    response = requests.get(url)
    data = response.json()
    serializer = ProductSerializer(data=data, many=True)
    
    if request.method == 'POST':
        for product in data:
            product['cost'] = product.get('price')
            product['name'] = product.get('title')
            product['photo'] = product.get('image')
        
    
        if serializer.is_valid():
            serializer.save()
            return redirect('products:home')
    context = {'products': serializer.initial_data}
    return render(request, 'api/fetch_api_products.html', context)

class ProductList(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            # Fetch data from the FakeStoreAPI
            url = 'https://fakestoreapi.com/products/category/electronics'
            response = requests.get(url)
            data = response.json()
        
            for product in data:
                product['cost'] = product.get('price')
                product['name'] = product.get('title')
                product['photo'] = product.get('image')
                if(product.get('category') == 'electronics'):
                    product['category'] = "others"


            # Serialize the data and validate it and save
            if request.method == "POST":
                serializer = ProductSerializer(data=data, many=True)
                serializer.is_valid(raise_exception=True)
                products = serializer.save()
 
        
                # Return response with list of uploaded products
                #return Response(ProductSerializer(products, many=True).data)
                message = {'message': 'Products added successfully! Go to http://localhost:8000 '}
                return Response(message)
    
    def get(self, request):
        # Return a list of all products
        if request.user.is_superuser:
            url = 'https://fakestoreapi.com/products/category/electronics'
            response = requests.get(url)
            data = response.json()
            serializer = ProductSerializer(data=data, many=True)

            if serializer.is_valid():
                responseData = serializer.data
            return Response(responseData)
        else:
            messages.warning(request, 'Only admin can perform this task. Please login as admin.')
            return redirect("products:home")