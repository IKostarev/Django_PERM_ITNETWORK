# Generated by Django 4.0.4 on 2022-05-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_car_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, height_field=500, unique=True, upload_to='back/uploads', verbose_name='Изображение машины', width_field=500),
        ),
    ]
