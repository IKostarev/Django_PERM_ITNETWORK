from django.shortcuts import render
from . import models


def car_set(request):
    car = models.Car.objects.all()
    buyer = models.Buyer.objects.all()

    context = {
        'title': 'Список автомобилей',
        'car': car,
        'buyer': buyer,
    }

    return render(request, template_name='back/index.html', context=context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

    else:
        return render(request, template_name='back/login.html', context={})


def logout(request):
    pass

