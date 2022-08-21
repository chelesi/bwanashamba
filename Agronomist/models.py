from django.db import models
from customer.models import customer

# Create your models here.
class Agronomist(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE,default="")
    First_Name = models.CharField(max_length = 30)
    Middle_Name = models.CharField(max_length = 30)
    Last_Name =models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)
    College  = models.CharField(max_length = 50)
    Experience = models.TextField(max_length = 200)
    Certificate_Copy =models.ImageField(upload_to='static/img/')
    
def _str_(self):
    return self.First_Name
#One to many relationship so customers model will reference experts model
#class customer(models.Model):
   # First_Name = models.CharField(max_length = 30)
   # Last_Name  = models.CharField(max_length = 30)
   # Last_Name  = models.CharField(max_length = 30)
   # Upload_Photo = models.FileField()
   # Price = models.CharField(max_length = 200)
    #Location = models.CharField(max_length = 50)
    #Phone = models.CharField(max_length = 10)
   # agronomist = models.ForeignKey(Agronomist, on_delete=models.CASCADE)


    #def _str_(self):
      #  return self.First_Name