from django.db import models

from product.models.family import Family


class SubFamily(models.Model):
    label = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.label