from django.contrib.auth.models import Agroengineer


class AgroengineerForm(forms.ModeForm):
    First_Name = models.CharField(max_length = 30)
    Middle_Name = models.CharField(max_length = 30)
    Last_Name =models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 10)
    College  = models.CharField(max_length = 50)
    Experience = models.TextField(max_length = 200)
    Certificate_Copy =models.FileField()
    
    class Meta:
 model = AgroengineerForm
 fields = ('First_Name, 'Middle_Name', 'Last_Name','location',' Phone','College',' Experience','Certificate_Copy')