from django.db import models

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self):
        return self.name
