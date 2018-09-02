from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied

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


