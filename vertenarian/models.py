from django.db import models
from datetime import datetime
from customer.models import customer


class Vertenarian(models.Model):
    customer= models.ForeignKey(customer, on_delete=models.DO_NOTHING,default="")
    First_Name = models.CharField(max_length = 30)
    Middle_Name = models.CharField(max_length = 30)
    Last_Name =models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)
    College  = models.CharField(max_length = 50)
    Experience = models.TextField(max_length = 200)
    Certificate_Copy =models.FileField(max_length = 4,default="")

    def __str__(self):
        return self.First_Name

# Create your models here.
#class Vertenarian(models.Model):
    #First_Name = models.CharField(max_length = 30)
    #Middle_Name = models.CharField(max_length = 30)
    #Last_Name =models.CharField(max_length = 30)
    #location = models.CharField(max_length = 50)
    #Phone = models.CharField(max_length = 10)
   # College  = models.CharField(max_length = 50)
    #Experience = models.TextField(max_length = 200)
    #Certificate_Copy =models.FileField()
    
#def _str_(self):
   # return self.First_Name

#One to many relationship so customers model will reference experts model
#class customer(models.Model):
    #First_Name = models.CharField(max_length = 30)
    #Last_Name  = models.CharField(max_length = 30)
    #Upload_Photo = models.FileField()
    #Price = models.CharField(max_length = 300)
    #Location = models.CharField(max_length = 50)
    #Phone = models.CharField(max_length = 15)
    #agroengineer= models.ForeignKey(Vertenarian, on_delete=models.CASCADE)


    #def _str_(self):
        #return self.First_Name