from django.utils import timezone

from django.db import models

from product.models.subFamily import SubFamily


class Product(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField(null=True)
    subFamily = models.ForeignKey(SubFamily, default='', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.label
