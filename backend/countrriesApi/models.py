from locale import currency
from pickletools import long1
from django.db import models
from pytz import timezone

# Create your models here.

class Countries(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(max_length=255)
    iso3 = models.CharField(max_length=255)
    iso2 = models.CharField(max_length=255)
    numeric_code = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    currency_name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=255)
    tld = models.CharField(max_length=255)
    native = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    emoji = models.CharField(max_length=255)
    emojiU = models.CharField(max_length=255)


class States(models.Model):
    state_id = models.IntegerField()
    name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    country_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    state_code = models.CharField(max_length=255)
    latitute = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

class Cities(models.Model):
    city_id = models.IntegerField()
    name = models.CharField(max_length=255)
    state_id = models.IntegerField()
    state_code = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    country_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    wikiDataId = models.CharField(max_length=255)