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
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class RevokeTokenView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    authentication_classes = [TokenAuthentication]
    model = None  # wajib di-override di subclass

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        """Bikin serializer dinamis sesuai model"""
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
    required_permission_codes = ["view_territorieswithemployees"]


class DepletedCategoryView(BaseReportView):
    model = DepletedCategory
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_depletedcategory']


class FragileProductsView(BaseReportView):
    model = FragileProducts
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_fragileproducts']


class EuropeanProductAveragePriceView(BaseReportView):
    model = EuropeanProductAveragePrice
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_europeanproductaverageprice']


class FavouriteShipperView(BaseReportView):
    model = FavouriteShipper
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_favouriteshipper']


class TotalEmployeeInEveryRegionView(BaseReportView):
    model = TotalEmployeeInEveryRegion
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_totalemployeeineveryregion']


class GeneralPhoneBookView(BaseReportView):
    model = GeneralPhoneBook
    permission_classes = [HasPermissionCode]
    required_permission_codes = ['view_generalphonebook']
