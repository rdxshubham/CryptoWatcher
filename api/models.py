from django.db import models


# Create your models here.

class CryptoCurrency(models.Model):
    id = models.AutoField(primary_key=True)
    currency_symbol = models.CharField(max_length=10)
    currency_name = models.CharField(max_length=50)
    date = models.DateField()
    txVolume = models.DecimalField(max_digits=50, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=8)
