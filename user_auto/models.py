from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Машина пользователя --------------------------------------------------------------
class Car(models.Model):
    STEERING_WHEEL_CHOICES = (
        (1, 'Левый'),
        (2, 'Правый'),
    )
    WHEEL_DRIVE_TYPE_CHOICES = (
        (1, 'Передний'),
        (2, 'Задний'),
        (3, 'Полный'),
    )


    brand = models.CharField(max_length=50, default=None, verbose_name='Марка')
    model = models.CharField(max_length=50, default=None, verbose_name='Модель')
    engine = models.CharField(max_length=50, default=None, null=True, blank=True, verbose_name='Двигатель')
    transmission = models.CharField(max_length=50, default=None, null=True, blank=True, verbose_name='Коробка передач')
    steering_wheel =  models.PositiveSmallIntegerField(choices=STEERING_WHEEL_CHOICES, null=False)
    wheel_drive_type =  models.PositiveSmallIntegerField(choices=WHEEL_DRIVE_TYPE_CHOICES, null=False)

    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name="CarOwner", verbose_name='Владелец Машины', blank = False, null = False)


    def __str__(self):
        return self.brand + self.model