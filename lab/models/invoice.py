from django.db import models
from .customer import Customer
from .agent import Agent, Doctor
from .lab import Test

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    test = models.ManyToManyField(Test)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return f'Invoice {self.id} for {self.customer.name}'
