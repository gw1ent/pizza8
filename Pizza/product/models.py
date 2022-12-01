from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=24, verbose_name="Название")
    price = models.IntegerField(validators=[MaxValueValidator(9999, message="Не может быть больше, чем 9999")], verbose_name="Цена")
    description = models.TextField(null=True, max_length=110, verbose_name="Описание")
    weight = models.IntegerField(validators=[MaxValueValidator(1000, message="Не может быть больше, чем 1000")], verbose_name="Вес")
    cm = models.IntegerField(default=25, validators=[MaxValueValidator(40, message="Не может быть больше, чем 40")], verbose_name="Диаметр")
    image = models.ImageField(upload_to='images', null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')