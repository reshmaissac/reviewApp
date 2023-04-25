from django.urls import path
from products.views import ProductList
from . import views


app_name = "products"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/',views.detail,name="detail"),
    path('allreviews/<int:id>/',views.allreviews,name="allreviews"),
    path('addproducts/',views.add_products,name="add_products"),
    path('getproducts/',views.getProducts,name="getProducts"),
    path('api-products/', ProductList.as_view(), name='api-products'),

    path('viewReview/<int:id>', views.viewReview, name="viewReview"), 
    path('edit/<int:id>', views.editReview, name="edit"), 
    path('delete/<int:id>', views.destroyReview), 
    
   


]