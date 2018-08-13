from django.db import models

class Carousel(models.Model):
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.image)