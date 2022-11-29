from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class CustomUser(AbstractUser):
    firstName = models.CharField(verbose_name='Имя', null=True, max_length=30)
    secondName = models.CharField(verbose_name='Фамилия', null=True, max_length=30)
    phoneNumber = PhoneField(verbose_name='Номер телефона', blank=True)
    address = models.CharField(verbose_name='Адрес', null=True, max_length=30)
    roleId = models.IntegerField(null=True, default=0)



