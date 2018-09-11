from django.db import models
from django.utils import timezone
from datetime import datetime


class Carousel(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.carousel_id)


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_quantity = models.IntegerField(default=0)
    design = models.ImageField(null=True, blank=True)
    report_date = models.DateTimeField(default=datetime.now, blank=True)
    modeofpayment = models.CharField(null=True, max_length=256, choices=[('Bank', 'Bank'), ('Meetup', 'Meetup')])
    shipment = models.CharField(null=True, max_length=256, choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')])

    def __str__(self):
        return self.modeofpayment, str(self.report_id)

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'
    category_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=32)
    description = models.CharField(max_length=120)


    def __str__(self):
        return self.productname

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    item_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.item_id)



