from django.shortcuts import render
from .models import USAEmployeePhoneBook, TerritoriesWithAllEmployees, DepletedCategory, FragileProducts, EuropeanProductAveragePrice, FavouriteShipper, TotalEmployeeInEveryRegion, GeneralPhoneBook

# Create your views here.

def home(request):
    return render(request, 'reports/home.html')

def usa_employee_phone_book(request):
    data = USAEmployeePhoneBook.objects.all()
    return render(request, 'reports/usa_employee_phone_book.html', {'data': data, 'title': 'USA Employee Phone Book'})

def territories_with_all_employees(request):
    data = TerritoriesWithAllEmployees.objects.all()
    return render(request, 'reports/territories_with_all_employees.html', {'data': data, 'title': 'Territories With All Employees'})

def depleted_category(request):
    data = DepletedCategory.objects.all()
    return render(request, 'reports/depleted_category.html', {'data': data, 'title': 'Depleted Category'})

def fragile_products(request):
    data = FragileProducts.objects.all()
    return render(request, 'reports/fragile_products.html', {'data': data, 'title': 'Fragile Products'})

def european_product_average_price(request):
    data = EuropeanProductAveragePrice.objects.all()
    return render(request, 'reports/european_product_average_price.html', {'data': data, 'title': 'European Product Average Price'})

def favourite_shipper(request):
    data = FavouriteShipper.objects.all()
    return render(request, 'reports/favourite_shipper.html', {'data': data, 'title': 'Favourite Shipper'})

def total_employee_in_every_region(request):
    data = TotalEmployeeInEveryRegion.objects.all()
    return render(request, 'reports/total_employee_in_every_region.html', {'data': data, 'title': 'Total Employee In Every Region'})

def general_phone_book(request):
    data = GeneralPhoneBook.objects.all()
    return render(request, 'reports/general_phone_book.html', {'data': data, 'title': 'General Phone Book'})
    