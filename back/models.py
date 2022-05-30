from enum import unique

from django.contrib.auth.models import AbstractBaseUser

from django.db import models
from back.user_manager import MyCustomUserManager



class Car(models.Model):
    car_number = models.CharField(verbose_name='Номер машины', unique=True, max_length=9, db_index=True)
    car_color = models.CharField(verbose_name='Цвет машины', max_length=32)
    car_brand = models.CharField(verbose_name='Бренд машины', max_length=32)
    car_model = (
        (1, 'Седан'),
        (2, 'Универсал'),
        (3, 'Хетчбэк'),
        (4, 'Лифтбэк'),
        (5, 'Лимузин'),
        (6, 'Пикап'),
        (7, 'Минивэн'),
        (8, 'Купе'),
        (9, 'Четырёхдверное купе'),
        (10, 'Масл кар'),
        (11, 'Кабриолет'),
        (12, 'Фаэтон'),
        (13, 'Ландо'),
        (14, 'Кроссовер'),
        (15, 'Родстер'),
        (16, 'Внедорожник'),
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=car_model)
    car_price = models.FloatField(verbose_name='Цена машины', default=0)
    is_sell_now = models.BooleanField(default=True)
    car_image = models.ImageField(unique=True, blank=True, verbose_name='Изображение машины в формате JPG', upload_to='back/templates/back/uploads')

    created_at = models.DateTimeField(verbose_name='Дата и время создания машины', auto_now=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления машины', auto_now_add=True)

    class Meta:
        db_table = 'car'


class Buyer(models.Model):
    name = models.CharField(verbose_name='Имя покупателя', max_length=32)
    money = models.IntegerField(verbose_name='Количество денег', default=0)

    cars = models.ManyToManyField(Car)

    class Meta:
        db_table = 'buyer'


class CarChop(models.Model):
    address = models.CharField(verbose_name='Адрес магазина', max_length=300)
    is_opening = models.BooleanField(default=True)

    cars = models.ManyToManyField(Car)
    buyers = models.ForeignKey(Buyer, on_delete=models.CASCADE)


class MyCustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = MyCustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    class Meta:
        db_table = 'mycustomuser'