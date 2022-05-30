from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as sing_in, logout as sing_out

from back.serializer import CarsSerializer
from . import models
from rest_framework import generics



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
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = authenticate(request, username=email, password=password)
        else:
            context.update({'error': 'Форма содержит пустые поля!'})

        if user is not None and user.is_active:
            sing_in(request, user)
            return redirect(to=reverse(''))
        else:
            context.update({'error': 'Пользователь не активен'})
    else:
        return render(request, template_name='back/login.html', context={})


def logout(request):
    sing_out(request)
    path = request.GET.get('path', None)

    if path is None:
        path = '/'

    return redirect(path)


class CarsAPIView(generics.ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = CarsSerializer