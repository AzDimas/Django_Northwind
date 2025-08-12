from django.contrib import admin
from django.urls import path
from reports import views
from reports import views_auth

urlpatterns = [

    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # AUTH API
    path('auth/login/', views.ObtainTokenView.as_view(), name='api-login'),
    path('auth/logout/', views.RevokeTokenView.as_view(), name='api-logout'),
    path("api/verify-token/", views.VerifyTokenView.as_view(), name="verify-token"),
    path('login/', views_auth.login_page, name='login_page'),

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

    path('usaemployee/html/', views.usa_employee_phone_book_html, name='usa_employee_phone_book_html'),
    path('territories/html/', views.territories_with_all_employees_html, name='territories_with_all_employees_html'),
    path('depletedcategory/html/', views.depleted_category_html, name='depleted_category_html'),
    path('fragileproducts/html/', views.fragile_products_html, name='fragile_products_html'),
    path('europeanproduct/html/', views.european_product_avg_price_html, name='european_product_avg_price_html'),
    path('favouriteshipper/html/', views.favourite_shipper_html, name='favourite_shipper_html'),
    path('regionemployee/html/', views.total_employee_in_every_region_html, name='total_employee_in_every_region_html'),
    path('generalphonebook/html/', views.general_phone_book_html, name='general_phone_book_html'),
    path('forbidden/', views.forbidden_page, name='forbidden_page'),
]
