from django.db import models

class Lab(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    altanative_phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Discount(models.Model):
    TYPE_CHOICE = (
        ('FLAT', 'Flat'),
        ('PERCENTAGE', 'Percentage')        
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, default='PERCENTAGE')
    amount = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class TestGroup(models.Model):
    type = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self) -> str:
        return self.type

class Test(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(TestGroup, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()
    time = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    




