from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.name
