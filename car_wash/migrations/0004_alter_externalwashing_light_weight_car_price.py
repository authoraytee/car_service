# Generated by Django 4.0.4 on 2022-06-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0003_alter_drycleaning_light_weight_car_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalwashing',
            name='light_weight_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='sdkgjlskdjg'),
        ),
    ]
