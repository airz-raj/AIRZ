from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oppp.urls')),  # Ensure the app name matches exactly
]