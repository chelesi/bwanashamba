from django.db import models
#from Agroengineer.models import Agroengineer
# Create your models here
class customer(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_Name  = models.CharField(max_length = 30)
    Upload_Photo = models.FileField()
    Price = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)
    #agroengineer= models.ForeignKey(Agroengineer, on_delete=models.CASCADE)

    def _str_(self):
        return self.First_Name