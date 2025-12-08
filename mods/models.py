import json
from os import write
from .modsdownload import data_list
from django.db import models
import os




class Mody(models.Model):
    mody_id = models.AutoField(primary_key=True)
    mody_date = models.DateTimeField(auto_now=True)
    mody_stare = models.FileField(upload_to="mody_stare")
    mody_nowe = models.FileField(upload_to="mody_nowe")





















    def __str__(self):
        return str(self.mody_id)









# Create your models here.
