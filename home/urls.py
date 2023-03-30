from django.urls import path
from . import views
app_name = 'home'
urlpatterns =[
    
    path('about/', views.about, name='home-about'),
    path('contact/', views.contact, name='home-contact'),
]