from django.db import models

# Create your models here.

#Iwant kilimo to be referenced as home page
class kilimo(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_Name  = models.CharField(max_length = 30)
    Upload_Photo = models.FileField()
    Price = models.CharField(max_length = 50)
    Location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)

    def _str_(self):
        return self.First_Name