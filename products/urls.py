from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/',views.detail,name="detail"),
    path('allreviews/<int:id>/',views.allreviews,name="allreviews"),
    path('addproducts/',views.add_products,name="add_products"),

    
    path('edit/<int:id>', views.edit), 
    path('delete/<int:id>', views.destroy), 
    
   


]