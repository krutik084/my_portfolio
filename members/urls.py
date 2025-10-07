from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='home'),
    path('members/', views.member_list, name='members'),
    path('contact/', views.contact, name='contact')
]