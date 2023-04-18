from django.db import models


class Client(models.Model):
    """A client model"""

    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    first = models.CharField(max_length=100, blank=False, null=False, help_text='First name')
    last = models.CharField(max_length=100, blank=False, null=False, help_text='Last name')

    def __str__(self):
        return self.first + self.last

    class Meta: #no_qa
        verbose_name = "Client"
        verbose_name_plural = "Clients"