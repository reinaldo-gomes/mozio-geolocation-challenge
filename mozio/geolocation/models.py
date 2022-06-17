from django.db import models


class Provider(models.Model):
    LANGUAGE_CHOICES = [
        ('ENGLISH', 'English'),
        ('FRENCH', 'French'),
        ('SPANISH', 'Spanish'),
        ('MANDARIN', 'Mandarin'),
        ('HINDI', 'Hindi'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'U.S. Dollar'),
        ('CAD', 'Canadian Dollar'),
        ('EUR', 'European Euro'),
        ('GBP', 'British Pound'),
        ('CHF', 'Swiss Franc'),
    ]
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    language = models.CharField(max_length=20, null=False, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=255, null=False, choices=CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    geolocation = models.JSONField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
