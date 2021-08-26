from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "NSS, MMMUT"
admin.site.site_title = "Welcome to admin portal"
admin.site.index_title = "Welcome to NSS, MMMUT"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

