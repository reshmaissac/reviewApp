from django.urls import path
from api.views import ProductList
from api.views import get_fakestore_data
from django.conf.urls.static import static
from django.conf import settings

app_name = "api"
urlpatterns = [
    # other URL patterns...
    #path('api/', include(router.urls)),
     path('api-products/', ProductList.as_view(), name='fetch_products'),
     path('get-fakestore-data/', get_fakestore_data, name='get_fakestore_data'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)