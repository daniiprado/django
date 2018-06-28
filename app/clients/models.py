from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=191)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, max_length=191)
    address = models.CharField(max_length=191)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
