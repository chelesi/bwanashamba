from django.db import models
from customer.models import customer
from datetime import datetime
#Model from listing starts here


class Agroengineer(models.Model):
    customer= models.ForeignKey(customer, on_delete=models.DO_NOTHING, default="")
    First_Name = models.CharField(max_length = 30)
    Middle_Name = models.CharField(max_length = 30)
    Last_Name =models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)
    College  = models.CharField(max_length = 50)
    Experience = models.TextField(max_length = 200)
    Certificate_Copy =models.FileField(upload_to='photos/%Y/%m/%d/')
    #Sphoto_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    

    def __str__(self):
        return self.First_Name






# Create your models here.
#class Agroengineer(models.Model):
   # First_Name = models.CharField(max_length = 30)
   # Middle_Name = models.CharField(max_length = 30)
   # Last_Name =models.CharField(max_length = 30)
   # location = models.CharField(max_length = 50)
    #Phone = models.CharField(max_length = 10)
   # College  = models.CharField(max_length = 50)
   # Experience = models.TextField(max_length = 200)
    #Certificate_Copy =models.FileField()
    
#def _str_(self):
  #  return self.First_Name

#One to many relationship so customers model will reference experts model
#class customer(models.Model):
   # First_Name = models.CharField(max_length = 300)
    #Last_Name  = models.CharField(max_length = 300)
    #Upload_Photo = models.FileField()
   # Price = models.CharField(max_length = 100)
    #Location = models.CharField(max_length = 50)
    #Phone = models.CharField(max_length = 10)
    #Agroengineer= models.ForeignKey(customer, on_delete=models.CASCADE)


    #def _str_(self):
       # return self.First_Name