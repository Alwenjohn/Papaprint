from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from datetime import datetime

user = get_user_model()

class OrderProducts(models.Model):
    Status = models.CharField(max_length=256, choices=[('Completed', 'Completed'), ('Shipment Pending', 'Shipment Pending'), ('Payment Pending', 'Payment Pending'), ('Problem', 'Problem')])
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    Amount = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    payment = models.CharField(max_length=256, choices=[('Paid', 'Paid'), ('Unprocessed', 'Unprocessed'), ('Capture Failed', 'Capture Failed')])

    def __str__(self):
        return self.Status