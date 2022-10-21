from django.db import models
from datetime import datetime

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    # DOB = datetime.date()
    DOB = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'