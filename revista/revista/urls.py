from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('allauth/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
]
