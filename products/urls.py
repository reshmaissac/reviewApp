from django.urls import path
from . import views

<<<<<<< HEAD

app_name = "products"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/',views.detail,name="detail"),
    path('addproducts/',views.add_products,name="add_products"),
   # path('editproducts/<int:id>/',views.edit_products,name="edit_products"),
    # path('deleteproducts/<int:id>/',views.delete_products,name="delete_products"),
   


=======
urlpatterns =[
    path('', views.home, name='home-home'),
    path('about/', views.about, name='home-about'),
    path('contact/', views.contact, name='home-contact'),
    path('products/', views.products, name='products-product001'),
>>>>>>> 8e34b7b (Linked product001 to test integration.)
]