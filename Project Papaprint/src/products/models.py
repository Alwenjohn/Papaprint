from django.db import models

class Carousel(models.Model):
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.image)


class Categoryproducts(models.Model):
        class Meta:
            verbose_name_plural = 'categories'

        productname = models.CharField(max_length=32)

        def __str__(self):
            return self.productname


class Itemproducts(models.Model):
    Category = models.ForeignKey(Categoryproducts, on_delete=models.PROTECT)
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Description