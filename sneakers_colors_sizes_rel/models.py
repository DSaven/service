from django.db import models

from colors.models import Colors
from sizes.models import Sizes
from sneakers.models import Sneakers


class SneakersColorsSizesRel(models.Model):
    id_relation = models.AutoField(primary_key=True)
    id_sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    id_color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    id_size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
