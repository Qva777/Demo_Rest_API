from rest_framework import serializers
from .models import Car


class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        """Выводит список из перечисленых значений"""
        model = Car
        fields = ('id', 'vin', 'color', 'breand', 'user')


class CarDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'
