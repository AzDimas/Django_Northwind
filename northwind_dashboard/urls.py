from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),  # semua URL reports pindah ke reports/urls.py
]
