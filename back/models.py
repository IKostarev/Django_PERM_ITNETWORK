from django.db import models



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
    car_price = models.FloatField
    is_sell_now = models.BooleanField(default=True)

    created_at = models.DateTimeField(verbose_name='Дата и время создания машины', auto_now=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления машины', auto_now_add=True)

    class Meta:
        db_table = 'car'