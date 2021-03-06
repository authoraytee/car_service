# Generated by Django 4.0.4 on 2022-06-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0005_alter_drycleaning_light_weight_car_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drycleaning',
            name='washing_object',
            field=models.CharField(default=None, max_length=50, verbose_name='Объект мойки'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='washing_object',
            field=models.CharField(default=None, max_length=50, verbose_name='Объект мойки'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='washing_object',
            field=models.CharField(default=None, max_length=50, verbose_name='Объект мойки'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='washing_object',
            field=models.CharField(default=None, max_length=50, verbose_name='Объект мойки'),
        ),
    ]
