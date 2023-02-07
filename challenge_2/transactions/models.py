from django.db import models
# import csv

# Create your models here.

#class TransactionsTypes()

class Transactions(models.Model):
    type = models.CharField(max_length=255)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cpf = models.TextField(max_length=11)
    card = models.TextField(max_length=12)
    hour = models.TimeField()
    owner = models.TextField()  
    name = models.TextField()   
    
