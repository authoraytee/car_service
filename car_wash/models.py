from django.db import models


# Внешняя мойка --------------------------------------------------------------
class ExternalWashing(models.Model):
    # Отбойник \ Мойка кузова \ Комплексная мойка и т.д. 
    washing_object = models.CharField(max_length=50, default=None, verbose_name='Объект мойки')

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name='Цена для легкового автомобиля')
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для универсала")
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для минивэна")
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для внедорожника")
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для микроавтобуса")

    def __str__(self):
        return self.washing_object


# Внутренняя мойка ----------------------------------------------------------
class InternalWashing(models.Model):
    # Стекла \ Коврики \ Пылесос салона и т.д.
    washing_object = models.CharField(max_length=50, default=None, verbose_name='Объект мойки')

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name='Цена для легкового автомобиля')
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для универсала")
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для минивэна")
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для внедорожника")
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для микроавтобуса")

    def __str__(self):
        return self.washing_object


# Полировка -----------------------------------------------------------------
class Polishing(models.Model):
    # Полировка кузова \ Чернение шин и т.д. 
    washing_object = models.CharField(max_length=50, default=None, verbose_name='Объект мойки')

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name='Цена для легкового автомобиля')
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для универсала")
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для минивэна")
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для внедорожника")
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для микроавтобуса")

    def __str__(self):
        return self.washing_object


# Химчистка -----------------------------------------------------------------
class DryCleaning(models.Model):
    # Потолок \ Пол \ Салон и т.д.
    washing_object = models.CharField(max_length=50, default=None, verbose_name='Объект мойки')

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name='Цена для легкового автомобиля')
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для универсала")
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для минивэна")
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для внедорожника")
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, verbose_name="Цена для микроавтобуса")


    def __str__(self):
        return self.washing_object