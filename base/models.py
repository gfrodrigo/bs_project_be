from django.db import models


# Create your models here.

class Business(models.Model):
    tax_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    annual_revenue = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
