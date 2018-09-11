from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator

user = get_user_model()

class OrderedProduct(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_fname = models.CharField(max_length=30)
    order_mname = models.CharField(max_length=30)
    order_lname = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    order_email = models.EmailField(unique=True)
    contact_regex = RegexValidator(regex=r'^(09|\+639)\d{9}$', message="Phone number must be entered in the format: 09 or '+639'. Up to 9 digits allowed.")
    contact_number = models.CharField(validators=[contact_regex], max_length=17, blank=True)
    order_status = models.CharField(max_length=256, choices=[('Completed', 'Completed'), ('Shipment Pending', 'Shipment Pending'), ('Payment Pending', 'Payment Pending'), ('Problem', 'Problem')])
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_amount = models.IntegerField()
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    payment = models.CharField(max_length=256, choices=[('Paid', 'Paid'), ('Unprocessed', 'Unprocessed')])

    def __str__(self):
        return '%s %s' % (self.order_fname, self.order_lname)
