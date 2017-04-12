# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Address(models.Model):

    country = models.CharField(max_length=254)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=254)
    postal_num = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)

    
class Crib(models.Model): 
    address = models.CharField(max_length=254) #models.OneToOneField(Address) #Une adress = 1 Crib et vice versa
    number_of_rooms = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cribs/static/cribs_pictures/', blank=True) 
    #A concatener avec IDCrib
    



class Guest(models.Model):
    email = models.EmailField()
    last_name = models.CharField(max_length=50)
    fist_name = models.CharField(max_length=50)
    address = models.CharField(max_length=254) #models.OneToOneField(Address)
    image = models.ImageField() #Not sure
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    min_number_of_cribmates = models.PositiveSmallIntegerField()
    max_number_of_cribmates = models.PositiveSmallIntegerField()
    min_price = models.PositiveSmallIntegerField()
    max_price = models.PositiveSmallIntegerField()
    desiredLocation = models.CharField(max_length=100) #Just the city for the moment




