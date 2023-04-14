from django.urls import path
from . import views
app_name = 'home'
urlpatterns =[
    path('home/', views.home, name='home-home'),
    path('about/', views.about, name='home-about'),
    path('contact/', views.contact, name='contact'),
]