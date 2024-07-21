from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=15, null=True, blank=True)
    commission=models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Agent(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=15, null=True, blank=True)
    commission=models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class PatientDetails(models.Model):
    GENDER_CHOICES=(
        ("MALE", 'Male'),
        ("FEMALE", 'Female'),
        ("OTHERS", 'Others'),
    )
    name=models.CharField(max_length=150)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=15, null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    age=models.SmallIntegerField()
    weight=models.FloatField(null=True, blank=True)
    height=models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class TestCategory(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class TestDetails(models.Model):
    name=models.CharField(max_length=150)
    test_category=models.ForeignKey(TestCategory, on_delete=models.CASCADE) 
    description=models.TextField(null=True, blank=True)
    price=models.FloatField()

    def __str__(self) -> str:
        return self.name
    
class Discount(models.Model):
    name=models.CharField(max_length=150)
    rate=models.IntegerField(null=True, blank=True)
    max_discount=models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Report(models.Model):
    invoice_no=models.CharField(max_length=20, unique=True)
    patient=models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    agent=models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    tests=models.ManyToManyField(TestDetails)
    discount=models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    sample_date=models.DateTimeField()
    report_date=models.DateTimeField()
    total_price=models.FloatField()

    def __str__(self) -> str:
        return self.invoice_no
    

    


