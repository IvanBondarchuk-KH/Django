from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('stats/', views.stats, name='stats'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('news/', views.news, name='news'),
    path('schedule/', views.schedule, name='schedule'),
    path('reviews/', views.reviews, name='reviews'),
    path('ebooks/', views.ebooks, name='ebooks'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
    path('kids/', views.kids, name='kids'),
    path('cooperation/', views.cooperation, name='cooperation'),
]