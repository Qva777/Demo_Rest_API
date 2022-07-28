from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    """Модели/поля"""
    vin = models.CharField(verbose_name='VIN', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64)
    brand = models.CharField(verbose_name='Бренд', max_length=64)
    CAR_TYPE = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Купе'),
        (4, 'Универсал'),
    )
    car_type = models.IntegerField(verbose_name='Тип:', choices=CAR_TYPE)
    user = models.ForeignKey(User, verbose_name='Пользователь:', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        """Строковое представление"""
        return self.brand

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
