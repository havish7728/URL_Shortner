from django.urls import path
from .import views

urlpatterns = [
    path('', views.urlShort, name='url_shorten'),  # Corrected path for urlShort view
    path('<slug:slugs>/', views.urlRedirect, name='url_redirect'),  # Corrected path for urlRedirect view
]
