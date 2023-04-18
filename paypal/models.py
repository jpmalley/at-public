from django.db import models

# Create your models here.
class PayPalTransaction(models.Model):
    
    transaction_id = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
    )
    
    status = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
    )
    
    buyer_first_name = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
    )
    
    buyer_last_name = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
    )

    buyer_email = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
    )

    associated = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    def __str__(self):
        return self.transaction_id + self.buyer_email

    class Meta: #no_qa
        verbose_name = "PayPal Transaction"
        verbose_name_plural = "PayPal Transactions"