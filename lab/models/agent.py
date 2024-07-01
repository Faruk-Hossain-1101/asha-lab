from django.db import models
from .lab import Discount


class Doctor(models.Model):
    name = models.CharField(max_length=150)
    expaties = models.CharField(max_length=200, null=True, blank=True, default='')
    degree = models.CharField(max_length=200, null=True, blank=True, default='')
    address = models.CharField(max_length=150, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) -> str:
        return self.name
    
class Agent(models.Model):
    name = models.CharField(max_length=100)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) -> str:
        return self.name
    

