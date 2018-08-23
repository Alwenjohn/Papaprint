from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    productname = models.CharField(max_length=32)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.productname

class Item(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)
    Brandname = models.CharField(max_length=32)
    description = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()


    def __str__(self):
        return self.description

