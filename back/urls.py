from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_set, name = 'car_set'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]