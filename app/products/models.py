from django.db import models
from clients.models import Client

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=2500)
    category = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Favorite(models.Model):
    user = models.ForeignKey(Client, on_delete='cascade')
    product = models.ForeignKey(Product, on_delete='cascade')

    class Meta:
        verbose_name='Favorite'
        verbose_name_plural='Favorites'
        
    def __str__(self):
        return '{} {}'.format(self.user.name, self.product.name)
