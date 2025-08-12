from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import (
    USAEmployeePhoneBook, TerritoriesWithAllEmployees, DepletedCategory,
    FragileProducts, EuropeanProductAveragePrice, FavouriteShipper,
    TotalEmployeeInEveryRegion, GeneralPhoneBook
)
from .permissions import HasRole, HasPermissionCode

# =============================
# LOGIN & LOGOUT
# =============================
class ObtainTokenView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class RevokeTokenView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerifyTokenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        
        # 1. Verifikasi token sudah dilakukan oleh TokenAuthentication
        # 2. Kumpulkan semua permission user
        all_permissions = set(user.get_all_permissions())

        # 3. Tambahkan permission dari role jika ada profile
        if hasattr(user, 'profile'):
            for role in user.profile.roles.all():
                for perm in role.permissions.all():
                    all_permissions.add(f"{perm.content_type.app_label}.{perm.codename}")

        # 4. Dapatkan path yang sedang diakses dari frontend
        requested_path = request.data.get('requested_path', '')  # Diambil dari body request
        
        # 5. Mapping path ke permission yang dibutuhkan
        path_permission_map = {
            '/generalphonebook/html/': 'reports.view_generalphonebook',
            '/usaemployee/html/': 'reports.view_usaemployeephonebook',
            '/territories/html/': 'reports.view_territorieswithallemployees',
            '/depletedcategory/html/': 'reports.view_depletedcategory',
            '/fragileproducts/html/': 'reports.view_fragileproducts',
            '/europeanproduct/html/': 'reports.view_europeanproductaverageprice',
            '/favouriteshipper/html/': 'reports.view_favouriteshipper',
            '/regionemployee/html/': 'reports.view_totalemployeeineveryregion',
        }

        # 6. Cek permission khusus jika path diminta
        if requested_path:
            required_permission = path_permission_map.get(requested_path)
            if required_permission and required_permission not in all_permissions:
                return Response(
                    {
                        "valid": False,
                        "detail": "Forbidden",
                        "required_permission": required_permission
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

        # 7. Return response sukses
        return Response({
            "valid": True,
            "username": user.username,
            "permissions": sorted(all_permissions)
        })


# =============================
# VIEW UNTUK ADMIN SAJA (ROLE)
# =============================
class AdminOnlyView(APIView):
    permission_classes = [HasRole]
    authentication_classes = [TokenAuthentication]
    required_roles = ['Admin']

    def get(self, request):
        return Response({"ok": True, "message": "Halo Admin"})


# =============================
# BASE REPORT VIEW
# =============================
class BaseReportView(generics.ListAPIView):
    """
    Semua report view wajib punya:
    - model (Django model)
    - required_permission_codes (list permission code)
    Otomatis pakai HasPermissionCode.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasPermissionCode]
    model = None
    required_permission_codes = []

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        """Serializer dinamis sesuai model"""
        Meta = type('Meta', (), {'model': self.model, 'fields': '__all__'})
        serializer_class = type(f'{self.model.__name__}Serializer', (serializers.ModelSerializer,), {'Meta': Meta})
        return serializer_class


# =============================
# VIEW REPORTS (Permission Per-View)
# =============================
class USAEmployeePhoneBookView(BaseReportView):
    model = USAEmployeePhoneBook
    required_permission_codes = ["view_usaemployeephonebook"]


class TerritoriesWithAllEmployeesView(BaseReportView):
    model = TerritoriesWithAllEmployees
    required_permission_codes = ["view_territorieswithallemployees"]


class DepletedCategoryView(BaseReportView):
    model = DepletedCategory
    required_permission_codes = ['view_depletedcategory']


class FragileProductsView(BaseReportView):
    model = FragileProducts
    required_permission_codes = ['view_fragileproducts']


class EuropeanProductAveragePriceView(BaseReportView):
    model = EuropeanProductAveragePrice
    required_permission_codes = ['view_europeanproductaverageprice']


class FavouriteShipperView(BaseReportView):
    model = FavouriteShipper
    required_permission_codes = ['view_favouriteshipper']


class TotalEmployeeInEveryRegionView(BaseReportView):
    model = TotalEmployeeInEveryRegion
    required_permission_codes = ['view_totalemployeeineveryregion']


class GeneralPhoneBookView(BaseReportView):
    model = GeneralPhoneBook
    required_permission_codes = ['view_generalphonebook']


# =============================
# HTML RENDER VIEWS (Opsional pakai login_required)
# =============================
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def home(request):
    return render(request, 'reports/home.html')

@login_required
@permission_required('reports.view_usaemployeephonebook', raise_exception=True)
def usa_employee_phone_book_html(request):
    data = USAEmployeePhoneBook.objects.all()
    return render(request, 'reports/usa_employee_phone_book.html', {
        'title': 'USA Employee Phone Book',
        'data': data
    })

@login_required
@permission_required('reports.view_territorieswithallemployees', raise_exception=True)
def territories_with_all_employees_html(request):
    data = TerritoriesWithAllEmployees.objects.all()
    return render(request, 'reports/territories_with_all_employees.html', {
        'title': 'Territories With All Employees',
        'data': data
    })

@login_required
@permission_required('reports.view_depletedcategory', raise_exception=True)
def depleted_category_html(request):
    data = DepletedCategory.objects.all()
    return render(request, 'reports/depleted_category.html', {
        'title': 'Depleted Category',
        'data': data
    })

@login_required
@permission_required('reports.view_fragileproducts', raise_exception=True)
def fragile_products_html(request):
    data = FragileProducts.objects.all()
    return render(request, 'reports/fragile_products.html', {
        'title': 'Fragile Products',
        'data': data
    })

@login_required
@permission_required('reports.view_europeanproductaverageprice', raise_exception=True)
def european_product_avg_price_html(request):
    data = EuropeanProductAveragePrice.objects.all()
    return render(request, 'reports/european_product_average_price.html', {
        'title': 'European Product Average Price',
        'data': data
    })

@login_required
@permission_required('reports.view_favouriteshipper', raise_exception=True)
def favourite_shipper_html(request):
    data = FavouriteShipper.objects.all()
    return render(request, 'reports/favourite_shipper.html', {
        'title': 'Favourite Shipper',
        'data': data
    })

@login_required
@permission_required('reports.view_totalemployeeineveryregion', raise_exception=True)
def total_employee_in_every_region_html(request):
    data = TotalEmployeeInEveryRegion.objects.all()
    return render(request, 'reports/total_employee_in_every_region.html', {
        'title': 'Total Employee in Every Region',
        'data': data
    })

@login_required
@permission_required('reports.view_generalphonebook', raise_exception=True)
def general_phone_book_html(request):
    data = GeneralPhoneBook.objects.all()
    return render(request, 'reports/general_phone_book.html', {
        'title': 'General Phone Book',
        'data': data
    })


def forbidden_page(request):
    return render(request, 'reports/forbidden.html')