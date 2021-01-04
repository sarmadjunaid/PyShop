from django.db import models

# a model defined for products


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

# a model defined for discounts


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField()