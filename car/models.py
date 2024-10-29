from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name

class Car(models.Model):
    image = models.ImageField(upload_to='static',null=True)
    name = models.CharField(max_length=50)
    product_date = models.DateField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name