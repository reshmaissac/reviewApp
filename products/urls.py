from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/',views.detail,name="detail"),
    path('addproducts/',views.add_products,name="add_products"),
    path('products/', views.products, name='products-product001'),
   # path('editproducts/<int:id>/',views.edit_products,name="edit_products"),
    # path('deleteproducts/<int:id>/',views.delete_products,name="delete_products"),