# Generated by Django 4.1.3 on 2022-11-29 06:52

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_address_alter_customuser_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=30, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='firstName',
            field=models.CharField(max_length=30, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='roleId',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='secondName',
            field=models.CharField(max_length=30, null=True, verbose_name='Фамилия'),
        ),
    ]