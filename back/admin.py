from django.contrib import admin

from back.models import Car, Buyer, CarChop, User


admin.site.register(User)
admin.site.register(Car)
admin.site.register(Buyer)
admin.site.register(CarChop)