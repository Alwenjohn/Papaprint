from django.db import models
from django.utils import timezone
from datetime import datetime

class Reports(models.Model):
    quantity = models.IntegerField(default=0)
    design = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    modeofpayment = models.CharField(max_length=256, choices=[('Bank', 'Bank'), ('Meetup', 'Meetup')])
    shipment = models.CharField(max_length=256, choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')])

    def __str__(self):
        return self.modeofpayment


