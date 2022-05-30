from django.contrib import admin
from django.urls import path, include
from back import urls as back_urls
from back.views import CarsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(back_urls)),
    path('api/v1/cars', CarsAPIView.as_view())
]
