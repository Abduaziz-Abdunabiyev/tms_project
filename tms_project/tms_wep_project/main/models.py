from django.db import models

class PlannedLoad(models.Model):
    custom_load_number = models.CharField(max_length=50, blank=True, null=True)
    customer = models.CharField(max_length=255)

    shipper = models.CharField(max_length=255)
    pickup_date = models.DateField()
    pickup_instructions = models.TextField(blank=True, null=True)

    consignee = models.CharField(max_length=255)
    delivery_date = models.DateField()
    delivery_instructions = models.TextField(blank=True, null=True)

    bol = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Load {self.custom_load_number} - {self.customer}"
