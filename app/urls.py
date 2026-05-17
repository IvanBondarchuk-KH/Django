from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('students/', views.students, name='students'),
    path('profile/', views.profile, name='profile'),
    path('sales/', views.sales, name='sales'),
]