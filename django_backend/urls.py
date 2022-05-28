from django.contrib import admin
from django.urls import path, include
from back import urls as back_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(back_urls)),
]
