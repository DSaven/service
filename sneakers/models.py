from django.db import models


class Sneakers(models.Model):
    id_sneaker = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    price = models.IntegerField()
