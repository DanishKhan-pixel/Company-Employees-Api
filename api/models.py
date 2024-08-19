from django.db import models

# Create your models here.
#  crteating the companyapi

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('name','alpha'),
                                                  ('location','islamabad'),
                                                  ('about','about ')))
    
    add_date=models.DateField(auto_now=True)
    activa=models.BooleanField(default=True)

    def __str__(self):
        return self.name +'--'+ self.location 

# creating Employee  model
class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    about=models.TextField()
    position =models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('developer','python developer'),
        ('Project','manager')

    ))
    company=models.ForeignKey(company,on_delete=models.CASCADE)
