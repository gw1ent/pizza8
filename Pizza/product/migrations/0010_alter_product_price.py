# Generated by Django 4.1.3 on 2022-12-01 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_cm_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=4, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
