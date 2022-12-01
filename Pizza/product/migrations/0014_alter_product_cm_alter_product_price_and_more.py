# Generated by Django 4.1.3 on 2022-12-01 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cm',
            field=models.IntegerField(default=25, validators=[django.core.validators.MaxValueValidator(40, message='Не может быть больше, чем 40')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999, message='Не может быть больше, чем 9999')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000, message='Не может быть больше, чем 1000')]),
        ),
    ]