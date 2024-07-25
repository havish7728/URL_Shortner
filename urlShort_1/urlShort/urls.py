from django.urls import path
from .import views

urlpatterns = [
    path('', views.url_shorten, name='url_shorten'),
    path('shorten/',views.shorten_success,name='shorten_success'),
    path('<slug>/', views.url_redirect, name='url_redirect')
]