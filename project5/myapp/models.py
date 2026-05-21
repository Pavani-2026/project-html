from django.db import models

from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    ram = models.IntegerField()

    def __str__(self):
        return self.name