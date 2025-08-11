"""
URL configuration for northwind_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usaemployee/', views.usa_employee_phone_book, name='usa_employee_phone_book'),
    path('territories/', views.territories_with_all_employees, name='territories_with_all_employees'),
    path('depletedcategory/', views.depleted_category, name='depleted_category'),
    path('fragileproducts/', views.fragile_products, name='fragile_products'),
    path('europeanproduct/', views.european_product_average_price, name='european_product_average_price'),
    path('favouriteshipper/', views.favourite_shipper, name='favourite_shipper'),
    path('regionemployee/', views.total_employee_in_every_region, name='total_employee_in_every_region'),
    path('generalphonebook/', views.general_phone_book, name='general_phone_book'),
]
