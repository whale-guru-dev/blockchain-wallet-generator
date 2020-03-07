from django.db import models

# Create your models here.
class CryptoAddress(models.Model):
    crypto_type = models.CharField(max_length=10)
    crypto_address = models.CharField(max_length=200, unique =  True)
    crypto_priv_key = models.CharField(max_length=200, unique =  True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)