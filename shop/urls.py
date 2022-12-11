from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_detail, prod_list
app_name = 'shop'

urlpatterns = [
    path('', prod_list, name='all_products'),
    path('<uuid:category_id>/', prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)