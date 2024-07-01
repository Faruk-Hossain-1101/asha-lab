from django.db import models

class Customer(models.Model):
    ID_CHOICES = (
        ('AADHAR', 'Aadhar'),
        ('VOTER', 'Voter'),
        ('PASSPORT', 'Passport'),
        ('OTHERS', 'Others')
    )
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    id_type = models.CharField(max_length=20, choices=ID_CHOICES, null=True, blank=True)
    id_number = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE)


    def __str__(self) -> str:
        return self.name
    
    
