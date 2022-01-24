from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_numbers, name='addnums'),
    path('addnumbers', views.add_numbers_page, name='addnumspage'),
    path('', views.home, name='home')
]