from django.db import models


# Внешняя мойка --------------------------------------------------------------
class ExternalWashing(models.Model):
    # Отбойник \ Мойка кузова \ Комплексная мойка и т.д. 
    washing_object = models.CharField(max_length=50, default=None)

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)

    def __str__(self):
        return self.washing_object


# Внутренняя мойка ----------------------------------------------------------
class InternalWashing(models.Model):
    # Стекла \ Коврики \ Пылесос салона и т.д.
    washing_object = models.CharField(max_length=50, default=None)

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)

    def __str__(self):
        return self.washing_object


# Полировка -----------------------------------------------------------------
class Polishing(models.Model):
    # Полировка кузова \ Чернение шин и т.д. 
    washing_object = models.CharField(max_length=50, default=None)

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)

    def __str__(self):
        return self.washing_object


# Химчистка -----------------------------------------------------------------
class DryCleaning(models.Model):
    # Потолок \ Пол \ Салон и т.д.
    washing_object = models.CharField(max_length=50, default=None)

    light_weight_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    universal_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minivan_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    suv_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    minibus_car_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)


    def __str__(self):
        return self.washing_object