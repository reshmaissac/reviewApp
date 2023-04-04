from django.urls import path
from api.views import fetch_products
from api.views import get_fakestore_data

app_name = "api"
urlpatterns = [
    # other URL patterns...
    #path('api/', include(router.urls)),
     path('fetch-products/', fetch_products, name='fetch_products'),
     path('get-fakestore-data/', get_fakestore_data, name='get_fakestore_data'),
]