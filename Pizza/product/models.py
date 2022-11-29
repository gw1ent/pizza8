from django.db import models
from django.conf import settings
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.IntegerField(default=0)
    calories = models.FloatField(max_length=5, default=0)
    weight = models.FloatField(default=0)
    cm = models.IntegerField(default=25)
    image = models.ImageField(upload_to='images', null=True)
    index = models.IntegerField(verbose_name='Индекс', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list', args=[str(self.id)])