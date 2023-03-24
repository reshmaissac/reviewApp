from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
	query = request.GET.get("title")
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

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact Us'})