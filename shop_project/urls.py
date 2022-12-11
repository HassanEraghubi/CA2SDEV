"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import product_detail, prod_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('<uuid:category_id>/', prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', product_detail, name='product_detail'),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('vouches/', include('vouchers.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)