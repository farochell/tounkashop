from django.db import models


class Family(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
