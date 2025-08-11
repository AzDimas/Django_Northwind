from django.contrib import admin
from django.urls import path
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH API
    path('auth/login/', views.ObtainTokenView.as_view(), name='api-login'),
    path('auth/logout/', views.RevokeTokenView.as_view(), name='api-logout'),

    # ADMIN ONLY
    path('admin-only/', views.AdminOnlyView.as_view(), name='admin-only'),

    # REPORTS API
    path('usaemployee/', views.USAEmployeePhoneBookView.as_view(), name='usa_employee_phone_book'),
    path('territories/', views.TerritoriesWithAllEmployeesView.as_view(), name='territories_with_all_employees'),
    path('depletedcategory/', views.DepletedCategoryView.as_view(), name='depleted_category'),
    path('fragileproducts/', views.FragileProductsView.as_view(), name='fragile_products'),
    path('europeanproduct/', views.EuropeanProductAveragePriceView.as_view(), name='european_product_average_price'),
    path('favouriteshipper/', views.FavouriteShipperView.as_view(), name='favourite_shipper'),
    path('regionemployee/', views.TotalEmployeeInEveryRegionView.as_view(), name='total_employee_in_every_region'),
    path('generalphonebook/', views.GeneralPhoneBookView.as_view(), name='general_phone_book'),
]
