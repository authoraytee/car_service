# Generated by Django 4.0.4 on 2022-06-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Коробка передач'),
        ),
    ]