from django.db import models


class Sizes (models.Model):
    id_size = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=45)
    price_coef = models.FloatField(null=True, default=None)
