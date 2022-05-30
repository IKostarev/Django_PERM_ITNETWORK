from django.contrib import admin

from back.models import Car, Buyer, CarChop, MyCustomUser


admin.site.register(MyCustomUser)
admin.site.register(Car)
admin.site.register(Buyer)
admin.site.register(CarChop)