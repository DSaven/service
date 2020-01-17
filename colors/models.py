from django.db import models


class Colors(models.Model):
    id_color = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=45)
    price_coef = models.FloatField(null=True, default=None)