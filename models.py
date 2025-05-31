from django.db import models

class Browser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    residence_type = models.CharField(max_length=50)
    month_income = models.DecimalField(max_digits=10,decimal_places=2)
    previous_loan = models.BooleanField()
    marital_status = models.CharField(max_length=10)
    dependency = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

# Create your models here.
