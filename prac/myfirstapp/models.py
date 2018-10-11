# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import CharField

#Create your models here.
class  Stock(models.Model):
     ticker = models.CharField(max_length = 10)  # type: CharField
     open   = models.FloatField()
     close  = models.FloatField()
     volume = models.FloatField()

     def __str__(self):
        return self.ticker

# generating new models(assignment given by python...)

