# Generated by Django 4.0.4 on 2022-06-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0004_alter_externalwashing_light_weight_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drycleaning',
            name='light_weight_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для легкового автомобиля'),
        ),
        migrations.AlterField(
            model_name='drycleaning',
            name='minibus_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для микроавтобуса'),
        ),
        migrations.AlterField(
            model_name='drycleaning',
            name='minivan_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для минивэна'),
        ),
        migrations.AlterField(
            model_name='drycleaning',
            name='suv_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для внедорожника'),
        ),
        migrations.AlterField(
            model_name='drycleaning',
            name='universal_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для универсала'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='light_weight_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для легкового автомобиля'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='minibus_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для микроавтобуса'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='minivan_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для минивэна'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='suv_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для внедорожника'),
        ),
        migrations.AlterField(
            model_name='externalwashing',
            name='universal_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для универсала'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='light_weight_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для легкового автомобиля'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='minibus_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для микроавтобуса'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='minivan_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для минивэна'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='suv_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для внедорожника'),
        ),
        migrations.AlterField(
            model_name='internalwashing',
            name='universal_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для универсала'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='light_weight_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для легкового автомобиля'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='minibus_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для микроавтобуса'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='minivan_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для минивэна'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='suv_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для внедорожника'),
        ),
        migrations.AlterField(
            model_name='polishing',
            name='universal_car_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена для универсала'),
        ),
    ]