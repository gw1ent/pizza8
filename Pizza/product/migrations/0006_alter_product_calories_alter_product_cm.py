# Generated by Django 4.1.3 on 2022-11-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='calories',
            field=models.FloatField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='cm',
            field=models.IntegerField(default=25),
        ),
    ]
