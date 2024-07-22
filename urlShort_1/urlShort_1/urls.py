from django.contrib import admin
from django.urls import path, include
from urlShort import views  # Adjust this import as per your app structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlShort.urls')),  # Adjust app name and include statement as needed
]
