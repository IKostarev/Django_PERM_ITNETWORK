from dataclasses import field
from rest_framework import serializers
from back.models import Car

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car_number', 'car_color', 'car_brand', 'car_type', 'car_price', 'is_sell_now', 'car_image')