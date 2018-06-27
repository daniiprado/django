from django.db import models

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
