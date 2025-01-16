from django.db import models

# Create your models here.
class Member(models.Model):
    #id = models.AutoField(primary_key=True)
    bill_number = models.CharField(max_length=100, unique = True)
    details_received = models.BooleanField(default = False)
    date_received = models.DateField(null=True, blank=True)
    invoice_correct = models.BooleanField(null = True)
    date_corrected = models.DateField(null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class wronginvoice(models.Model):
    bill_number = models.CharField(max_length=100,unique = True)
    details_received = models.BooleanField(default = False)
    date_received = models.DateField(null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)